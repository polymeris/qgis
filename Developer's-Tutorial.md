> This document is an introduction to developing analytical backends or single modules for the QGIS Processing Framework, aimed at developers. It is work in progress, may contain errors and certainly many omissions. If you have questions, please contact me at <cpolymeris@gmail.com>

## The Processing Framework

The QGIS processing framework is written in python and consists of the following parts:

  * The framework itself, also known as processing _core_, which resides in `python/processing`.
  * The processing manager, implemented as a QGIS plugin, resides in `python/plugins/processingplugin`, responsible for the GUI side of things, like displaying the module tree panel, and module execution dialogs.
  * The analytical backends, also implemented as plugins, like the SAGA interface in `python/plugins/saga`

It is the [first part's API](http://polymeris.github.com/qgis/processing.html) we will be mostly concerned with in this tutorial, but because we are implementing a QGIS plugin, you should be familiar with [their development](http://www.qgis.org/wiki/Writing_Python_Plugins) and refer to the [general QGIS API](http://doc.qgis.org/head/), when necessary.

## A most basic module skeleton

Our first module will be called _GDAL algorithms demo_ and will implement one of the GDAL tools, contour, as an example.
The module's `__init__.py` file is easy, it will look like any other QGIS plugin:

``` python
def name():
    return "GDAL algorithms demo"
def description():
    return "Makes a GDAL algorithm available through the processing framework."
def version():
    return "Version 0.1"
def qgisMinimumVersion(): 
    return "1.0"
def authorName():
    return "Camilo Polymeris"
def classFactory(iface):
    import gdalalgorithms
    return gdalalgorithms.Plugin(iface)
```

Implementation of the plugin's `__init__` and `__unload__` methods in `gdalalgorithms.py` is also straightfoward, we actually do *nothing*. That is because, in general, we let the _processing manager_ plugin handle GUI stuff, as said above.

``` python
class Plugin:
    def __init__(self, iface):
        # save reference to the QGIS interface
        self.iface = iface
    def unload(self):
        pass
    def initGui(self):
        #TODO: implement this method
        pass
```

It is with the `initGui` & `modules` methods that things start to get interesting. Despite the name of the former method, we again do nothing GUI related, but instead initialize our sample module. Let's first add the required imports to the top of `gdalalgorithms.py`:

``` python
import processing
from processing.parameters import *

from osgeo import gdal
```

The `modules` method should simply return a set of modules, that is instances of the [`processing.Module`](http://polymeris.github.com/qgis/processing.html#Module) class, which contain metadata about each module, like name, description, tags and parameters. In this case, because we are defining only one module, we write:

``` python
    def modules(self):
        return [self.contourModule]
```

It is in the `initGui` method that we create this single module. We will implement the class later.

``` python
    def initGui(self):
        self.contourModule = ContourModule()
```

And then register our class with the framework:

``` python
        processing.framework.registerModuleProvider(self)
```

By now, your `gdalalgorithms.py` should look like this:

``` python
import processing

class Plugin:
    def __init__(self, iface):
        # save reference to the QGIS interface
        self.iface = iface
    def unload(self):
        pass
    def modules(self):
        return [self.contourModule]
    def initGui(self):
        self.contourModule = ContourModule()
        processing.framework.registerModuleProvider(self)
```

Now, that we have the basic module skeleton, we'll have to decide on an approach to implement our specific module. While using the QGIS Processing Framework, you will often have the chance to use either the provided classes (`Module`, `ModuleInstance`, `Parameter` and its subclasses), or implement your own.

## Defining a Module

In this example, I will subclass `Module` and `ModuleInstance`, to show you how it could be done, but keep in mind that this is not always necessary. It depends on how much you want to customize the behaviour of your backend.

So, **what are `Modules` and `ModuleInstances`?**, and what is the difference?

You can see the former as containers of metadata of modules and the later as actual modules preparing to run, running or stopped. That is, each object of type `Module` corresponds to a module with different _functionality_, while two objects of type `ModuleInstance` may have the same functionality and only differ in the _values of parameters_. Of course, a Module object is associated to each `ModuleInstance` object.

This distinction will become more apparent when we implement these classes, starting with `ContourModule`.
This module will have only two parameters: An input raster layer and an output vector layer. These are built-in parameter types, defined in `processing.paramters`

We create these parameters in the initializer:

``` python
class ContourModule(processing.Module):
    def __init__(self):
        self.inParam = RasterLayerParameter("Input raster")
        self.inParam.setRole(Parameter.Role.input)
        self.outParam = VectorLayerParameter("Output layer")
        self.outParam.setRole(Parameter.Role.output)
```

Easy, huh? There are more types of parameters, of course, and more options, but for now it will suffice.
Next we just call the parent `__init__` method (or use `super()`, if you prefer).

``` python
        processing.Module.__init__(self, "Contour", 
            description = "GDAL demo module",
            parameters = [self.inParam, self.outParam], tags = ["gdal"])
``` 

Each Module subclass should implement an `instance` method, to return the right type of `ModuleInstance`. The `ModuleInstance` class is very generic, and while it has access to the module's parameters, of course, since we are dealing with a specific module, we'll pass them manually.

``` python
    def instance(self):
        return ContourModuleInstance(self, self.inParam, self.outParam)
```

The code for `ContourModuleInstance` is only a bit longer. The init method is fairly self-explanatory, except for the last line:

``` python
class ContourModuleInstance(processing.ModuleInstance):
    def __init__(self, module, inParam, outParam):
        self.inParam = inParam
        self.outParam = outParam
        processing.ModuleInstance.__init__(self, module)
        QObject.connect(self,
            self.valueChangedSignal(self.stateParameter),
            self.onStateParameterChanged)
```

The `ModuleInstance.valueChangedSignal(parameter)` returns the Qt signal that is emitted when the parameters value changes. We are passing the pseudo-parameter `stateParameter` to the method, to know when the module's state changes from stopped to running.

We then connect this signal to the `self.onStateParameterChanged` slot, which we'll define next:

``` python
    def onStateParameterChanged(self, state):
        if state == StateParameter.State.running:
            inLayer = self[self.inParam]
            outLayer = self[self.outParam]
            self.contour(inLayer, outLayer)
            self.setState(StateParameter.State.stopped)
```

The parameter's value is passed to the slot, so we use this to determine if we are running the module, in which case we call `self.contour`, method that does the actual work. When this method returns we set the state to _stopped_, again.

Note that you could use this signals & slots mechanism to react to any change in parameter values, not just state. This allows you to e.g. modify your module on-the-fly or give feedback to the user.

## Making it tick

Finally, we just have to implement the `ContourModuleInstance.contour(in, out)` method. I have just adapted [the code from a script in GDAL's svn repository](http://svn.osgeo.org/gdal/trunk/autotest/alg/contour.py):
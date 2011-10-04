Python Library Documentation: module processing.moduleinstance in processing

# __NAME__

processing.moduleinstance - This module is part of the QGIS Processing Framework.

# __FILE__

/home/dimitri/.qgis/python/processing/moduleinstance.py

# __CLASSES__

PyQt4.QtCore.QObject(sip.wrapper)
    ModuleInstance

## class __ModuleInstance__
****************************************
Represents a single setup and execution of a module.


### data
****************************************
### descriptors
****************************************
### methods
****************************************
#### def __feedback__((self,), None, None, None):


#### def __module__((self,), None, None, None):


#### def __parameters__((self,), None, None, None):

Returns a dict of parameters to (default) values.

#### def __setFeedback__((self, fb, critical), None, None, (False,)):


#### def __setState__((self, state), None, None, None):


#### def __state__((self,), None, None, None):


#### def __valueChangedSignal__((self, param), None, None, (None,)):

Returns the signal emited when a parameter's value changes.
(Doesn't emit it)
The value is passed to the slot, not so the parameter.
If no parameter is specified, a "parametersChanged" signal is
returned which should be emitted when the parameter structure
changes, e.g. parameters are added, renamed or removed.


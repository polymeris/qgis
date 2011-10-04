What a QGIS Processing Framework could look like. Just a starting point to promote [discussion](http://lists.osgeo.org/pipermail/qgis-developer/2011-April/014057.html).

**In general, the implementation can extend this.** If the desired data type, widget, tag or feature is not supported, backends can implement it by subclassing or even talk directly to QGIS, as any plugin would.

Possible back-end implementations for:

* [SAGA](http://www.saga-gis.org/)
* [GRASS](http://grass.fbk.eu/)
* [Orfeo Toolbox](http://www.orfeo-toolbox.org/)
* [OSSIM](http://www.ossim.org)
* OGS' [WPS](http://www.opengeospatial.org/standards/wps)

QGIS side written in C++, Python bindings. Implementations for SAGA & other systems as plugins.
As simple as possible. Naming conventions are SAGA, which I am most familiar with, _process object_ is the OTB name for module, _category_ the GRASS name for library.

Modules are categorized in only one level of hierarchy ("libraries") & tagged.
The SAGA implementation would extract a number of relevant tags from the names of modules and libraries and their documentation, including wiki categories.

[[QGIS-relation.png]]

Note that the GUI part of the framework is handled in the processing plugin, while the logic is in core.

### General considerations

The QGIS side handles all GUI aspects (something like [this](http://wiki.orfeo-toolbox.org/upload/a/a6/Snapshot-qgis_plugin_ihm_v0_2.png) or [this](http://www2.udec.cl/~cpolymeris/QGIS_Screenshot_04032011.png)), and saving and loading parameters from file. The particular implementations handle loading and execution of modules. Which side handles format conversion? Either have the implementations list the formats they accept, and QGIS do conversion only if necessary, _or_, define an exchange format for raster, vector, and other data.

Martin commented on this:

 > Formats and format conversion: for import and export of map layers the framework should support
 > any layer loaded (or loadable) by QGIS. In case the library uses a different format for input/output,
 > it should take care of import/export.

### Parameters

See [[List of parameters]].

Can be nested using Parameters that are themselves lists of parameters. Only 2 levels of nesting recommended to not clutter GUI and keep scripting simpler.

There are basic and advanced parameters. Advanced parameters **must** always provide sensible default values. SAGA does not provide this information, though. Could be included in the wiki, perhaps.

### GUI considerations
[[http://www2.udec.cl/~cpolymeris/QGIS_Screenshot_04032011.png|width=640px]]

A GUI tree sorts modules by tag, showing only descriptive tags. Tags too frequent or too infrequenty to be useful are hidden. There is also a special tag for frequently used & recently used modules. Explicitely favorited modules are added to the frequently used list.

A central setting "Allways hide advanced module parameters" -- turns overall advanced parameter visibility on or off. If this option is not selected visibility is handled on a instance-per-instance case, using a toggle or switch.

Library names, module names, descriptions and tags can be searched from a single input box on top of the module tree.

A plugin can provide their own custom widgets, validators & types.
Interaction and feedback handled through the same mechanism as parameters: signals.

### Non-GUI considerations

The framework must work in a non-gui context: web, scripting. A Python API will be provided.

### Workflow
"Pipelining" (OTB term) ignored for now. Maybe it can be built on top later.
References: [vistrails](http://www.vistrails.org), [kepler](http://kepler-project.org)

Clearly defined types would help I think. Also some hint as what the modules do. E.g. _conversion_-only modules can be inserted & removed from the workflow by QGIS depending on other modules' required i/o formats.

While a simple _batch_ mode can be implemented by the user using the framework's Python API, ideally at a later point **vistrails** can be better integrated. This would make a powerful workflow engine for QGIS.

### Tentative list of tags
Case-insensitive.

* 2D
* 3D
* analysis
* classification
* database
* display
* export
* filter
* imagery
* import
* interactive
* paint
* photo
* postscript
* projection
* raster
* simulation
* statistics
* vector
* _favorite_
* _recently used_

Tags appear in tree according to weightening from occurrence. Non-descriptive, that is, too infrequent or too frequent tags hidden.

## Implementation priorities

Julien said:

> From my point of view, the Qgis common ground is all about :
>
> - getting raster/vector layers as input, and producing raster/vector layer as output.
> - having a Qt based interface using widgets which are as similar as possible when they represent similar concepts, which fit Qgis UI guidelines
> - having Python interfaces

Martin said:

> [...] A very important thing in projects like this one is to stay focused on the primary
> target and to keep the scope limited to a reasonable set of features.
> More bells and whistles can be typically added later.

## API
C++ implementation could use QString, QList, QPair, QValidator, QVariant and QVariant::Type as applicable.
[Current Python implementation.](https://github.com/polymeris/qgis/tree/master/python/processing)

Use same mechanism as plugins:

Module Methods:

* string name
* string description
* string version
* string qgisMinimumVersion
* string authorName
* list Library libraries

Need to specify required libraries/versions?

Overriden:

* ProcessingPlugin classFactory - creates a ProcessingPlugin that returns libraries calling the above method

### Module class
Methods:

* string getLabel
* string getDescription
* list string getTags
* list Parameter getParameters
* Parameter getState - conveinience for getParameters[state]

Member:

* Parameter class

### Parameter class
Member of Module
*Note*: Custom types can be added. See [QMetaType](http://doc.qt.nokia.com/4.7/qmetatype.html)

Methods:

* string getName
* string getDescription
* type getType
* role getRole
* userlevel getUserLevel
* bool isMandatory
* variant getDefaultValue

Members:

* enum userlevel: basic, advanced, ...
* enum role: input, ouput (read-only), option
* validator

### ModuleInstance class
Is serialized as equivalent Python command.

Constructor:

* ModuleInstance(Module, list variant options)
* ModuleInstance(python commands)

Methods:

* slot parameterValue(parameter, value)
* signal parametersChanged(module)
* Module getModule
* execute - fire parameterValue(state, running) signal
* string toPython

Member:

* enum state: init, running, paused, done

### Validator class
Method:

* state validate (string & input, int & pos )
  This virtual function returns Invalid if input is invalid according to this validator's rules, Intermediate if it is likely that a little more editing will make the input acceptable (e.g. the user types "4" into a widget which accepts integers between 10 and 99), and Acceptable if the input is valid. The function can change both input and pos (the cursor position) if required. (From QValidate)

Member:

* enum state: invalid, intermediate, acceptable
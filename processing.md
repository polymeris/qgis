Python Library Documentation: package processing

# __NAME__

processing - # -*- coding: utf-8 -*-

# __FILE__

/home/dimitri/.qgis/python/processing/__init__.py

# __PACKAGE CONTENTS__

apidoc
checkmodulesupport
markdowndoc
moduleinstance
parameters

# __CLASSES__

__builtin__.str(__builtin__.basestring)
    Tag
Framework
Module

## class __Framework__
****************************************
The Framework is instantiated in a singleton:
processing.framework.
This is the centerpiece of the QGIS Processing Framework, which
keeps track of all available modules through moduleproviders.
(See registerModuleProvider method)
It sorts these modules by tag and provides the model data for the
Processing Panel Plugin, which handles the GUI side of things.


### data
****************************************
__s__ = 'vector'
__standardTags__ = set(['2D', '3D', 'analysis', 'classification', 'database', 'display', ...])
### descriptors
****************************************
### methods
****************************************
#### def __moduleProviders__((self,), None, None, None):

Module providers are returned in a python set.

#### def __modules__((self,), None, None, None):

Returns complete set of registered modules by all module
providers.

#### def __modulesByTag__((self, tag), None, None, None):

Returns all modules that match the tag specified.

#### def __registerModuleProvider__((self, moduleprovider), None, None, None):

Register module providers with the framework.
moduleprovider must implement the modules() method,
which returns a list of modules.

#### def __representativeTags__((self,), None, None, None):

Returns list of tags that aren't too frequent or to infrequent
to be representative.
That is, cut tags that only apply to 2.5% of the modules or to
more than 15%.
In future, this criterion will be user-modifiable from the
settings dialog.

#### def __tagFrequency__((self,), None, None, None):

Return a dict of tag => relative tag frequency.
Relative tag ranges from 0.0 to 1.0, the latter identifing tags
that every module has.
This is a measure of how relevant a tag is.

#### def __unregisterModuleProvider__((self, moduleprovider), None, None, None):

Call this method to unregister a moduleprovider from your
backend's deinitialization code, e.g. unload() method.
It will return silently if the moduleprovider is not registered.

#### def __usedTags__((self,), None, None, None):

Return a set of all tags used by at least 1 module.
May contain standard tags and/or implementation-specific tags.

## class __Module__
****************************************
A processing module.
As a backend developer you will most likely want to subclass this.
As a user or script developer, get a module from the framework
singleton, then one or more ModuleInstances.
See ModuleInstace class for more information.

Attributes:
name -- this is the handle to the Module, and the name displayed
    in the GUI.
description -- this is a longer description of the module's
    functionality, may be multi-line and HTML-formatted.
tags -- this is a set of case-insensitive classificators of the
    module.
parameters -- this is a set of input & ouput parameters of different
    types. Control and feedback is also handled through this
    mechanism. See parameters module for more information.


### data
****************************************
### descriptors
****************************************
### methods
****************************************
#### def __description__((self,), None, None, None):

The modules description string.
If no description is provided on construction, returns an empty
string.

#### def __instance__((self,), None, None, None):

Return a new module instance.
Call this instead of the ModuleInstance constructor.
Backend implementations may want to override only this method
as an alternative to the whole class if your interface is simple
enough.

#### def __name__((self,), None, None, None):


#### def __parameters__((self,), None, None, None):

The module's parameters.
Specifiy on construction or override this method to provide your
own. Else raises an NotImplementedError.

#### def __tags__((self,), None, None, None):

The modules tags.
By default, this method searches for 'standard tags' in the
module's name & description. Dumb method, so reimplement if
possible.
To customize this, either indicate tags on construction or
override this method.

## class __Tag__
****************************************
Case insensitive strings for tag usage.


### data
****************************************
### descriptors
****************************************
__zfill__
S.zfill(width) -> string

Pad a numeric string S with zeros on the left, to fill a field
of the specified width.  The string S is never truncated.

### methods
****************************************

# __DATA__

__framework__ = <processing.Framework instance>


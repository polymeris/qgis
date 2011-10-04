## Second term

### Final report, August 20th

I am happy to say that this week saw many improvements in the QGIS Processing Framework and the interface to SAGA. Primarily, raster input and output works now, thanks to help from SAGA developer Volker Wichmann. Single band local QGIS rasters are transparently converted to SAGA format using GDAL, processed, and imported back into QGIS. Many things could be improved and features added, but the basic functionality is there.

To assess the progress of the interface, I have written a small script, which checks module support, as determined by parameter implementation. The programmatically collected stats, indicating support for 170 modules (40%) are published in the [[Module Support]] wiki page, while the [[Tested Modules]] page, maintained by Paolo, contains a list of SAGA modules that have actually been tested.

Work on a settings dialog has started. It is still unclear how many and which settings should be left to the user. Also on the GUI side, an about dialog was implemented, which displays the new processing icon by Robert Szczepanek.

[[processing64.png]]

In an effort to be consistent with the QGIS terminology, the string "raster" is now automatically substituted for instances of "grid" in each SAGA module's text: Names, tags, parameters and descriptions.

Less visible to the user, but still important, the SAGA code has been refactored a little. Work is still pending on this issue. Additionally, the plugin's objects are now managed in a cleaner way.

Validator and default value bugs have been fixed. Further testing is necessary.

Finally, due to rising interest in interfacing other libraries (GRASS, OTB) I have published the [API documentation on the framework](http://polymeris.github.com/qgis/processing.html) and started writing a [[Developer's Tutorial]].

Google Summer of Code 2011 is almost over, but it is my intention to continue maintaining this software, first focusing on polishing the available code and later adding more features: Support for further parameter types, interactive modules, and module instance serialization, among many other proposed.

### August 15th
This week I have implemented _Range parameters_ and tried to implemented the SAGA's _raster output_. To do this I have tried to solve various issues, mostly regarding specifying grid systems to the module. I have implemented a widget that allows the user to set a custom grid system and mechanisms to take the grid system from the input grids. The efforts haven't been enough, tough, SAGA modules keep outputting invalid rasters.
A [discussion concerning this issue](http://sourceforge.net/mailarchive/message.php?msg_id=27868820) is going on at the saga-gis-developer mailing list. I hope that with a little help I'll be able to solve this during this week.

Additionally I have solved a few bugs concerning _plugin initialization_, _string parameter_ conversion and _GUI_ issues.

The list of pending issues has been moved to the tracker provided by github, in preparation of further work after end of the GSoC project.

In case you are interested in testing the --still very experimental-- project, a [short document explaining installation and basic](https://github.com/polymeris/qgis/wiki/SAGA-Interface-HOWTO) usage is now available through the wiki.

As said, for next week, raster output implementation is of top priority. While this gets sorted out I'll complement the code's documentation, in particular the processing framework's.

### August 7th
I have implemented the feedback parameter, including the corresponding GUI changes.
Also completely rewrote the layer input & ouput mechanism, which is now working correctly for vectors and for local raster input.
Raster output requires setting the grid system parameter of saga modules, a task I'll consider as soon as possible.

Some other miscellaneous improvements where made, including the ability to set the SAGA path through a dialog, adding the familiar saga menu names as tags & the addition of a parameter list widget, in preparation of implementing the rest of this feature next week.

Most goals for the second term of GSoC are, thus, complete. Besides the mentioned, are remaining: Better code documentation & unit tests (which I'll leave for the extra week, if time permits) and module serialization which I'll tackle next.

### July 26th

I have fallen a bit behind schedule while trying to implement data exchange. Many issues have arisen, but finally vector output (from SAGA's perspective) is working. Neither input nor raster work yet.
Next, I'll consider the former, while also fixing some bugs in parameter selection (especially file & choices).

Having partially implemented data exchange, at least one SAGA module works: "Pythagoras' tree". Below is a screenshot of that module in action.

[[Pythagoras-Screenshot.png]]

There have also been some minor changes in GUI: Input & output parameters are now differentiated by the addition of a '>' symbol to the later, while optional parameter's labels appear in italics.

## First term
### Midterm report, July 11th

This week+, I polished different parts of the module dialog, adding specific widgets & callbacks (signals) for actions & value changes, including, e.g. a "FileSelector" widget for paths, and a combobox for available layers or module specific choices. (See screenshot below).

This will allow the modules to change the available parameters (and their presentation to the user) in reaction to value changes.

Also, the module instance's state (stopped, running, paused, etc.) mechanism was implemented on the processing side. This is yet invisible, because I haven't interfaced it to SAGA (see `moduleinstance.py`).

This being the last week of the first term, I also tried to look ahead a little to what expects us during the next few weeks, which are the most important things that are missing and how to implement them. With the help from other developers through the mailing list, I compiled [[a list thereof|Timeline]]. In summary, due during the next term, in my opinion, are:

  * Data exchange (passing vector & raster data from QGIS to the implementation, will be done with ogr/gdal), starting now.
  * Multiple value parameters
  * Logging & progress report
  * Module instance serialization (storing "presets" of module values), also as intermediate step to accessing the moduleinstance from a cleaner python API.
  * Better code documentation & unit tests.

I hope to also squeeze in some other minor parts (GUI things and such).

In conclusion, I think this has been a productive week and a very fun first term. I am grateful for all the friendly (and insightful) comments & criticism I have received. Thanks a lot!

[[Screenshot-0.6.png]]

### July 2nd

I have ported the parameter system to traits, but am not sure if I am taking the right approach. Dynamically generating the module definitions and instances is problematic using traits. A more elegant way would be to create a new python type for each module (perhaps using `type()`), subclassing `HasTraits`.

It seems difficult to advance from this stage of development, the last few weeks I have been writing and rewriting the same things, as understanding of the problem and requirements change.

I would very much appreciate comments on how to continue: Do you think traits is the way to go? If so, can you suggest cleaner ways to implement the framework?

### June 27th
This week I ported the module list to a MVC model using `QStandardItemModel`/`QTreeView`. I'll test it a bit more before pushing to faunalia's repo.

[Traits](http://code.enthought.com/projects/traits/) came up as an alternative to replace the parameter/validator system. Traits also provides methods for GUI creation (with a Qt backend).
This migration was suggested on the list and, so far, seems to be accepted.

I have studied the Traits documentation and started implementing relevant changes. This will consume most of my time next week.

### June 17th
This week the Framework's design saw many changes. Julien has started to experiment with interfacing it to the Orfeo Toolbox, and from the ensuing discussion the conclusions of creating a separate plugin for the framwork's gui, sort of a "module manager", now called processingplugin and removing some unnecessary classes were drawn. These things were implemented.
Also, a model-view interface will be used for the module list.

Some bugs were also fixed. A few new parameter types introduced. (String, Boolean, Choice)

No screenshot this week, but, the good news is you can see for yourself how it is coming along, since the **very experimental** plugins are now available through the [faunalia.it repo](http://www.faunalia.it/qgis/plugins.xml). Note that you most install "processingplugin" for the SAGA plugin to work. Many thanks to Giuseppe & Paolo for their help and providing the hosting.

Any comments welcome!

Next week I hope to catch up with validators, and move the module list to model-view.

### June 10th

I have added GUI elements for numeric parameters to the module dialogs as proof of the parameter system (a SpinBox):
[[Dialog-Screenshot.png]]

<i>Screenshot of the Ordinary Kringing module dialog</i>

In the process of implementing this, I have introduced the 'ModuleInstance' class, similar as described in the [[documentation|QGIS Processing Framework]] & encountered some difficulties posed by particularities of the Python language I was not aware of before.

Also, the build system works now (at least the basics) and a few bugs have been removed. Mostly I have tried to advance quickly (to get a working prototype) and certainly many bugs, in particular related to the UI, remain.

Next week, I hope to refine the constraints/validator mechanism and add a few more widgets for other cases.

### June 3rd
This week, I coded a GUI list of modules, sorted by tag (which in the case of SAGA are determined programmatically), plus the basics of a 'run module' dialog. I have started working on the parameter passing aspect of the framework.
I also set out to handle class generation for the GUI & installation of python files from cmake. Being inexperienced in cmake, this wil require further study & work.

Next week I intend to (as per the timeline), add GUI elements for the simplest cases of parameters and get the build system working.
[[Panel-Screenshot.png]]

**While there is no build system**, some comments on installing the framework & plugin:

> All the code is python. It resides in qgis/python/processing &
> qgis/python/plugins/saga.

> There are .ui (Qt designer XML) files in qgis/python/processing/gui,
> which must be converted to python, using the
> pyuic4 tool:

> pyuic4 panel.ui > ui_panel.py

> pyuic4 dialog.ui > ui_dialog.py

> I then symlinked qgis/python to ~/.qgis/python, so that qgis would
> read the latest version of the python script while developing. That
> works.`


### May 27th
During the first week of the proper coding period, I implemented registration for the saga plugin, plus loading libraries and creating module lists, using SAGA's python bindings. The framework provides a list of registered modules and associated tags. The next step will be to construct a tree in QGIS' gui.

## Community bonding period
### May 15th
During the past week, I have updated the [[Timeline]] and setup the development environment, including Python, the SAGA Python API & the git repo (now forked from [qgis/Quantum-GIS](https://github.com/qgis/Quantum-GIS).

The discussion on the mailing list hasn't continued, except for a few comments from developers of the SAGA and Vistrails projects, expresing they interest in interaction with the [[framework|QGIS Processing Framework]]. While some things are still unclear, I think development can begin, resolving any issues as they arise.

I received a 1-year student membership to ACM as part of the GSoC-bonus package, and have taken the opportunity to study a bit about python development methodologies through that channel.

During the remaining time of the community bonding period I expect to start coding some small parts of the project, to see if there are any problems with the development environment as it is, or if any issues with the design become apparent.

### May 5th
Upon learning on April 25 that I was selected for GSoC 2011 :D, my mentor, Paolo, informed me that there had been a discussion during the recently held Lisbon Hackfest to try and implement a more generic solution to processing in QGIS -- sort of a processing or analysis Framework. This in context of the Orfeo Toolbox team developing a interface to QGIS with similar requirements than my SAGA to QGIS interface.

The last week was spend discussing the design of this [[QGIS Processing Framework]] with the QGIS team and interested developers from other projects: a variety of valuable opinions came up, on topics ranging from the parameter types to be used in the API to GUI implementation details. I tried to collect the information as it crystallized in a sort of consensus in that wiki page. After a very intensive first few days, during the weekend the discussion seems to have suddenly calmed down. I have taken this as a sign that we have reached at least a plateau, a first stage of agreement. Surely many details must still be ironed-out, but in general I think we are going in the right direction, and issues can be resolved as they spring up during implementation.

As recommended, I am implementing the framework in Python, so that such changes in design can be addressed faster and with less effort. If necessary, either because of interoperability or performance concerns, a switch to C++ can be considered later, be it for the whole framework or a part of it. If this were the case, Python bindings would still have to be provided.

During the next week I plan to reformulate my timeline to accommodate the drastically changed goals of my project. I have also started formulating the API in Python.
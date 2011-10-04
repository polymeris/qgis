> This document is a basic guide to installing and testing the development version of the SAGA Modules interface for QGIS.
> While this is **experimental** software, not yet ready for production use, your help & feedback is very much appreciated. Please don't hesitate to send any comments on this document or the software to either the QGIS developers mailing list (<qgis-developer@lists.osgeo.org>) or my own e-mail(<cpolymeris@gmail.com>).
> Bugs can also be reported through the [Issue tracker](https://github.com/polymeris/qgis/issues).

### Requisites

To get the SAGA interface working, you need a recent version of [QGIS](www.qgis.org)(version 1.5 or up) with GDAL (version 1.7.0, at least) support, installed.

Additionally, you'll need to have the SAGA Python bindings installed.

If you are using _debian_, packages (python-saga) are available from the unstable repositories. On a debian _stable_ machine, you can locally install the `python-saga`, `lib-saga` and `libhpdf-2.2.1` packages from the unstable repos.

For _ubuntu_, there are packages available from [[https://launchpad.net/~johanvdw/+archive/saga-gis]] or (this will also add newer version of other gis applications, including qgis and gdal) [[https://launchpad.net/~ubuntugis/+archive/ubuntugis-unstable]]. In particular, the second rep with Ubuntu 11.04 installs everything smoothly, without the need for further config. The plugin has to be installed through usual QGIS Plugin installer.

See [[How to install the SAGA Python Bindings]] for further instructions.

### Installation of the plugins

There are two relevant plugins, which you can both install thorugh QGIS' Python plugin installer (_Plugins > Fetch python plugins..._ menu) and manage through the Plugin manager.

  * the _Processing Framework Manager_, aka processingplugin
  * the _SAGA Module interface_ plugin itself

### Plugin usage

After installation, the Processing Framework Manager should provide you with a new _Processing_ menu, which so far only has one item: a toggle to show and hide the list of plugins in a panel like the following.

[[Panel-Screenshot.png]]

If installation went ok & QGIS can find the SAGA libaries, the panel should display a list of modules, sorted by tags. Else, QGIS will ask you for the location of the SAGA libraries. To avoid having to provide this path on every QGIS start, you may want to set the MLB_PATH environment variable.

To run a module, double-click on the module's name in the list. A dialog asking for parameters should pop-up. Set the relevant parameters (some may be optional) and click on the _Execute_ button.

Currently, by far not all modules are supported. You may often encounter that some parameters are labeled 'Unsupported parameter of type ____'. We are working on it. If you want, you can add modules you have tested and work to the list of [[tested modules]].

### Troubleshooting & bug reports

The framework & interface are both in a very early state of development, so you'll probably encounter bugs and errors. To report these problems, please provide the python full backtraces, which should be displayed in a pop-up box after plugin crashes, together with the conditions that triggered the error.

In case you get segmentation faults (the whole program crashes), you may want to run QGIS in a terminal (console) or, if possible, debugger, to provider further data on the source of the bug.

Please use the project's [Issue tracker](https://github.com/polymeris/qgis/issues) or any of the mentioned e-mails (<qgis-developer@lists.osgeo.org> and/or <cpolymeris@gmail.com>) to report bugs. Help may also be available through the #qgis IRC channel on freenode.

Thanks a lot!
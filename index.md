# QGIS Processing Framework & SAGA Interface
In [QGIS](http://www.qgis.org/) there are [several analytical tools](http://www.qgis.org/wiki/Analytical_framework), mostly relying on external software. We plan to add a common framework, so every tool will fit in, and all tools could be used either individually or chained together.

In particular, this project aims at the creation of a QGIS plugin that makes it possible to run the versatile "System for Automated Geoscientific Analysis" ([SAGA GIS](http://www.saga-gis.org/)) modules from Quantum GIS. This plugin generates a GUI on-the-fly and runs the modules using the SAGA Python API, i.e. automates the process of information exchange between QGIS as a end-user interface and SAGA as an analytical tool.

**If you want to help _testing_ the interface, have a look at the [[SAGA Interface HOWTO]] for installation and usage instructions.** Thanks!

If you are _developer_ thinking of providing support for your processing library to QGIS, you may want to read the introductory [[Developer's Tutorial]], the [framework's API](http://polymeris.github.com/qgis/processing.html) and/or [[the design document|QGIS Processing Framework]] (a bit outdated, but still relevant).

Also, don't hesitate to contact [me](mailto:cpolymeris@gmail.com) or the [QGIS developers mailing list](http://lists.osgeo.org/mailman/listinfo/qgis-developer) for information, criticism or praise!

### Installation

  * [[QGIS Processing framework with SAGA|SAGA Interface HOWTO]] installation instructions

### Feedback

  * [Issue tracker](https://github.com/polymeris/qgis/issues)
  * QGIS Mailing lists: [users](http://lists.osgeo.org/mailman/listinfo/qgis-user), [developers](http://lists.osgeo.org/mailman/listinfo/qgis-developer)
  * Personal contact: [e-mail](mailto:cpolymeris@gmail.com), [Google+](https://plus.google.com/105255066783959366873)

### Development

  * Current [QGIS Processing Framework API](http://polymeris.github.com/qgis/processing.html)
  * [QGIS C++ API](http://qgis.org/api/)
  * [PyQGIS "cookbook"](http://www.qgis.org/pyqgis-cookbook/plugins.html)
  * [QGIS Developer's manual](http://www.qgis.org/wiki/Developers_Manual)
  * (Out-dated) [[QGIS Processing Framework]] design document

### SAGA specific
  * [SAGA](http://www.saga-gis.org/saga_api_doc/html/index.html)
  * [[Building & Installing|How to install the SAGA Python Bindings]]

### Other
  * [Prospective tools to use with the framework](http://www.qgis.org/wiki/Analytical_framework)
  * [Full table of contents of this wiki](https://github.com/polymeris/qgis/wiki/_pages)

[[Home-Title.png]]
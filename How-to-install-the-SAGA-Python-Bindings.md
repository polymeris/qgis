To run the SAGA interface to QGIS it is requiered to have the SAGA Python bindings installed. Packages distributed for Linux (as of writing) and Windows not always include this.

## Linux binaries
If you are using either debian or ubuntu install the packages using the debian "unstable" repositories or, in the latter case, getting them from [[https://launchpad.net/~johanvdw/+archive/saga-gis]] or [[https://launchpad.net/~ubuntugis/+archive/ubuntugis-unstable]].

This document explains how to build SAGA from sources. This will provide the SAGA command line and graphical applications, its modules and, most importantly, the Python bindings.

## Getting the sources
SAGA sources are available from the project's [site at sourceforge][SAGA sf]. Download the latest version (2.0.X) of the zipped sources or alternatively through subversion repository: `https://saga-gis.svn.sourceforge.net/svnroot/saga-gis/trunk/saga-gis`

Unzip the sources to the directory of your preference.

## Installing requisites under Linux
SAGA has some requisites which must be installed before compilation. Depending on your distribution, the procedure to get these may vary, but the requisites are the same, namely:

* swig (package name: `swig`)
* wxWidgets (package name: `libwxgtk2.8-dev`)
* gdal library (package name: `libgdal1-dev`)
* jasper library (package name: `libjasper-dev`)
* tiff library (package name: `libtiff-dev`)

Under debian, ubuntu or other debian-based distributions you can get all of the above (except swig) running `sudo apt-get build-dep saga`.

Also install the `build-essentials` package, which depends on all required build tools:

* GCC compiler with C++ support
* make, automake & libtool utilities

It is very likely that you have some or most of the above packages already installed.

## Compilation under Linux
Compilation should be straight-forward: First, change into the directory where you extracted the sources (`cd .../saga-gis/`) and run `autoreconf` or, if this fails: `aclocal && automake -a && autoconf`. This should generate a script called `configure`.

Run this script by executing:
`./configure --enable-unicode --enable-python`

The first argument configures the build for unicode, so that it matches the wx packages you installed before. It is unlikely, but if your wx packages are non-unicode, leave it out. The second argument configures the build to include the python bindings, what we are most interested in.

Finally, compile SAGA with the `make` command and install it running `sudo make install`.

If everything went ok, the SAGA applications will be installed under: `/usr/local/bin`, the modules under `/usr/local/lib/saga/` and the python bindings under `/usr/local/lib/python/`. To check it try running saga:
`saga_gui` or loading the Python bindings from the QGIS console: `import saga_api`.

## Getting requisites & compilation under Windows
At a later date I may post more detailed instructions, but for the moment, please see:

 * [Giovanni Allegri's experience building SAGA with Visual Studio][allegri]
 * Instructions at [SAGA's website][SAGA api on win]

[SAGA api on win]: http://sourceforge.net/apps/trac/saga-gis/wiki/Compiling%20SAGA%20Python%20Bindings%20on%20Windows
[SAGA sf]: http://sourceforge.net/projects/saga-gis/files/SAGA%20-%202.0/
[allegri]: http://lists.osgeo.org/pipermail/qgis-developer/attachments/20110411/34d70820/BUILDINGSAGAWITHVisualStudio2008Express2011-0001.odt
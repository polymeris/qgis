# -*- coding: utf-8 -*-

#	SAGA Modules plugin for Quantum GIS
#
#	__init__.py (C) Camilo Polymeris
#	
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
# 
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#       
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#   MA 02110-1301, USA.

theSAGAPlugin = None

def name():
    return "SAGA Module interface"

def description():
    return "Run the versatile SAGA modules. SAGA must be installed"
    
def icon():
    return "saga.png"
    
def version():
    return "Version 0.1"
    
def qgisMinimumVersion():
    return "1.0"
    
def authorName():
    return "Camilo Polymeris"
    
def classFactory(iface):
    try:
        import saga_api
    except ImportError:
        import PyQt4.QtGui
        window = iface.mainWindow()
        PyQt4.QtGui.QMessageBox.warning(window,
            window.tr("Could not find SAGA python bindings"),
            window.tr("<html>Could not find the Python bindings for "
                "SAGA, which are required to run the this module.<br/>"
                "See instructions on how to install them in the "
                "<a href=\"https://github.com/polymeris/qgis/wiki/"
                "How-to-install-the-SAGA-Python-Bindings\">"
                "QGIS SAGA interface wiki</a></html>"))
    from plugin import SAGAPlugin
    global theSAGAPlugin
    if not theSAGAPlugin:
        theSAGAPlugin = SAGAPlugin(iface)
    return theSAGAPlugin

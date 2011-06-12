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
from processing import framework
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def name():
    return "Processing Framework Module"

def description():
    return "QGis Processing Framework Manager"
    
def icon():
    return "saga.png"
    
def version():
    return "Version 0.1"
    
def qgisMinimumVersion():
    return "1.0"
    
def authorName():
    return "Camilo Polymeris"

class ProcessingPlugin:
    """ Processing plugin
    """
    def __init__(self, iface):
        self._iface = iface
    def initGui(self):
        self.menu = QMenu()
        self.menu.setTitle(QCoreApplication.translate("Processing", "Processing"))
        self.panel = QAction(QCoreApplication.translate("Processing", "&Panel"), self._iface.mainWindow())
        self.menu.addActions([self.panel])
        QObject.connect(self.panel, SIGNAL("triggered()"), self.showPanel)
        menu_bar = self._iface.mainWindow().menuBar()
        actions = menu_bar.actions()
        lastAction = actions[len(actions) - 1]
        menu_bar.insertMenu(lastAction, self.menu)
    def unload(self):
        pass
    def showPanel(self):
        framework.updateGui(self._iface)

def classFactory(iface):
    return ProcessingPlugin(iface)


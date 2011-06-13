# -*- coding: utf-8 -*-

#	QGIS Processing panel plugin.
#
#	__init__.py (C) Camilo Polymeris, Julien Malik
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
from ui import Panel
from PyQt4.QtCore import QObject, SIGNAL
from PyQt4.QtGui import QAction, QMenu

def name():
    return "Processing Framework Module"

def description():
    return "QGis Processing Framework Manager"
    
def icon():
    return "processing.png"
    
def version():
    return "Version 0.1"
    
def qgisMinimumVersion():
    return "1.0"
    
def authorName():
    return "Camilo Polymeris & Julien Malik"

class ProcessingPlugin:
    """ Processing plugin
    """
    def __init__(self, iface):
        self._iface = iface
        self.panel = None
    def initGui(self):
        self.menu = QMenu()
        self.menu.setTitle(self.menu.tr("Processing", "Processing"))
        self.panelAction = QAction(self.menu.tr("&Panel", "Processing"),
            self._iface.mainWindow())
        self.panelAction.setCheckable(True)
        self.menu.addAction(self.panelAction)
        QObject.connect(self.panelAction,
            SIGNAL("triggered(bool)"), self.showPanel)
        menuBar = self._iface.mainWindow().menuBar()
        menuBar.insertMenu(menuBar.actions()[-1], self.menu)
    def unload(self):
        pass
    def showPanel(self, visible = True):
        if not self.panel:
            self.panel = Panel(self._iface)
            QObject.connect(self.panel,
                SIGNAL("visiblityChanged(bool)"),
                self.panelAction.setChecked)
        self.panel.setVisible(visible)

def classFactory(iface):
    return ProcessingPlugin(iface)


# -*- coding: utf-8 -*-

#	SAGA Modules plugin for Quantum GIS
#
#	plugin.py (C) Camilo Polymeris
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

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

import saga_rc
from panel import Panel

class SAGAModulesPlugin:
    def __init__(self, iface):
	self.iface = iface
	self.panel = Panel(iface)

    def initGui(self):
	icon = QIcon(":/sagamodules/saga.png")
	self.action = QAction(icon,
	    "Show SAGA Modules",
	    self.iface.mainWindow())
	self.action.setCheckable(True)
	self.action.setWhatsThis("Show SAGA module list in side panel")
	self.action.setStatusTip("Show SAGA module list in side panel")
	QObject.connect(self.action,
	    SIGNAL("triggered(bool)"), self.panel.setVisible)
	QObject.connect(self.panel,
	    SIGNAL("visibilityChanged(bool)"), self.action.setChecked)
	self.separator = self.iface.pluginMenu().addSeparator()
	self.iface.pluginMenu().addAction(self.action)

    def unload(self):
	self.iface.pluginMenu().removeAction(self.separator)
	self.iface.pluginMenu().removeAction(self.action)

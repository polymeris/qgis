# -*- coding: utf-8 -*-

#	SAGA Modules plugin for Quantum GIS
#
#	panel.py (C) Camilo Polymeris
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

from PyQt4.QtGui import QDockWidget, QTreeWidgetItem
from PyQt4.QtCore import QObject, SIGNAL
from ui_panel import Ui_moduleListDock
from modulelist import ModuleList
import sagacommand
from dialog import Dialog

class Panel(QDockWidget, Ui_moduleListDock):
    def __init__(self, iface):
        QDockWidget.__init__(self, iface.mainWindow())
        self.iface = iface
        self.dialogs = list()
        self.setupUi(self)
        self.setFloating(False)
        ml = self.moduleList
        for l in sagacommand.getLibrariesReadable():
            item = QTreeWidgetItem(ml, l)
            for m in sagacommand.getModules(l[1]):
                QTreeWidgetItem(item, [m])
    	QObject.connect(self.moduleList,
			SIGNAL("itemActivated(QTreeWidgetItem *, int)"),
			self.onItemActivated)
    def onItemActivated(self, item, _):
        lib = item.parent()
        if lib is None:
            return
        dialog = Dialog(self.iface, lib.text(1), item.text(0))
        self.dialogs.append(dialog)
        dialog.show()

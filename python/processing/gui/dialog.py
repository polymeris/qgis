# -*- coding: utf-8 -*-

#	SAGA Modules plugin for Quantum GIS
#
#	dialog.py (C) Camilo Polymeris
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

from PyQt4.QtGui import QDialog
from ui_dialog import Ui_runDialog
import sagacommand

class Dialog(QDialog, Ui_runDialog):
    def __init__(self, iface, lib, module):
        QDialog.__init__(self)
        self.iface = iface
        self.module = module
        self.setupUi(self)
        self.setWindowTitle(self.windowTitle() + module)
        for p in sagacommand.getModuleParameters(lib, module):
			self.form.addRow(p.text, p.getWidget())

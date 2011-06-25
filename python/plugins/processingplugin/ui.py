# -*- coding: utf-8 -*-

#	QGIS Processing Framework
#
#	gui/__init__.py (C) Camilo Polymeris
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

from PyQt4.QtGui import QDockWidget, QTreeWidgetItem, QDialog
from PyQt4.QtGui import QSpinBox, QLineEdit, QCheckBox, QComboBox
from PyQt4.QtCore import QObject, SIGNAL, Qt
from ui_dialog import Ui_runDialog
from ui_panel import Ui_dock
import processing

class Panel(QDockWidget, Ui_dock):
    def __init__(self, iface):
        QDockWidget.__init__(self, iface.mainWindow())
        self._iface = iface
        self._dialogs = list()
        self.setupUi(self)
        tags = processing.framework.representativeTags()
        self.moduleList.setModel(framework)
    	QObject.connect(self.moduleList,
			SIGNAL("activated(QModelIndex)"),
			self.onItemActivated)
        self.setFloating(False)
        self._iface.addDockWidget(Qt.RightDockWidgetArea, self)
    def onItemActivated(self, ix):
        """ This slot pops up the relevant dialog. """
        mod = self.moduleList.data(ix, Module.ModulePointerRole)
        dialog = Dialog(self._iface, mod)
        self._dialogs.append(dialog)
        dialog.show()

class Dialog(QDialog, Ui_runDialog):
    def __init__(self, iface, module):
        QDialog.__init__(self, iface.mainWindow())
        self.moduleinstance = processing.ModuleInstance(module)
        self.setupUi(self)
        self.setWindowTitle(self.windowTitle() + " - " + module.name())
        self.text.setText(module.description())
        self._widgets = set()
        for param, value in self.moduleinstance.parameters().items():
            widget = self.widgetByType(param, value)
            self._widgets.add(widget)
            if widget is not None:
                self.form.addRow(param.name(), widget)
    def widgetByType(self, param, value):
        from processing.parameters import *
        try:
            w = param.widget(param, value)
            return w
        except AttributeError:
            pass
        pc = param.__class__
        if pc == NumericParameter:
            w = QSpinBox(None)
            w.setValue(value)
            return w
        if pc == BooleanParameter:
            w = QCheckBox(None)
            w.setChecked(value)
            return w
        if pc == ChoiceParameter:
            w = QComboBox(None)
            w.addItems(param.choices())
            w.setCurrentItem(value)
            return w
        w = QLineEdit(str(value), None)
        return w

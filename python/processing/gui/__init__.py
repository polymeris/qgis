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
from PyQt4.QtGui import QSpinBox
from PyQt4.QtCore import QObject, SIGNAL, Qt
from ui_dialog import Ui_runDialog
from ui_panel import Ui_dock
import processing

class Panel(QDockWidget, Ui_dock):
    def __init__(self, framework, iface):
        QDockWidget.__init__(self, iface.mainWindow())
        self._framework = framework
        self._iface = iface
        self._dialogs = list()
        self.setupUi(self)
        tags = framework.representativeTags()
        self.buildModuleList(tags)
    	QObject.connect(self.moduleList,
			SIGNAL("itemActivated(QTreeWidgetItem *, int)"),
			self.onItemActivated)
        self.setFloating(False)
    ## The TreeWidget's items:
    class TagItem(QTreeWidgetItem):
        """ First hierarchical level: order by tags """
        def __init__(self, parent, tag = "other"):
            QTreeWidgetItem.__init__(self, parent, [tag])
    class ModuleItem(QTreeWidgetItem):
        """ Second hierarchical level: modules by name """
        def __init__(self, module):
            QTreeWidgetItem.__init__(self,[module.name()])
            self._module = module
        def module(self):
            return self._module
    def buildModuleList(self, tags):
        """ Construct the tree of modules. """
        topNode = self.moduleList
        # a set of modules not yet added to the list
        pending = set(self._framework.modules())
        # add a node for each tag
        for tag in tags:
            tagNode = Panel.TagItem(topNode, tag)
            # and its children
            for mod in self._framework.modulesByTag(tag):
                modNode = Panel.ModuleItem(mod)
                tagNode.addChild(modNode)
                pending.discard(mod)
        # add non-tagged modules
        tagNode = Panel.TagItem(topNode)
        for mod in pending:
            modNode = Panel.ModuleItem(mod)
            tagNode.addChild(modNode)
    def onItemActivated(self, item, _):
        """ This slot pops up the relevant dialog. """
        if type(item) is Panel.ModuleItem:
            dialog = Dialog(self._iface, item.module())
            self._dialogs.append(dialog)
            dialog.show()

class Dialog(QDialog, Ui_runDialog):
    def __init__(self, iface, module):
        QDialog.__init__(self, iface.mainWindow())
        self.setupUi(self)
        self.setWindowTitle(self.windowTitle() + " - " + module.name())
        self.moduleinstance = processing.ModuleInstance(module)
        self._widgets = set()
        for param, value in self.moduleinstance.parameters().items():
            widget = self.widgetByType(param, value)
            self._widgets.add(widget)
            if widget is not None:
                print param.name()
                self.form.addRow(param.name(), widget)
                print self.form.count()
    def widgetByType(self, param, value):
        try:
            return param.widget(param, value)
        except AttributeError:
            pass
        try:
            print param.__class__
            typToWidget = {
                processing.parameters.NumericParameter: QSpinBox(None)
                }
            return typToWidget[param.__class__]
        except KeyError:
            return None

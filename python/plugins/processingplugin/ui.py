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

from PyQt4.QtGui import QDockWidget
from PyQt4.QtCore import QObject, SIGNAL, Qt
from traitsui.api import View
from ui_panel import Ui_dock
import processing

class Panel(QDockWidget, Ui_dock):
    def __init__(self, iface):
        QDockWidget.__init__(self, iface.mainWindow())
        self._iface = iface
        self._dialogs = list()
        self.setupUi(self)
        tags = processing.framework.representativeTags()
        self.buildModuleList(tags)
    	QObject.connect(self.moduleList,
			SIGNAL("itemActivated(QTreeWidgetItem *, int)"),
			self.onItemActivated)
        self.setFloating(False)
        self._iface.addDockWidget(Qt.RightDockWidgetArea, self)
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
        topNode.clear()
        # a set of modules not yet added to the list
        pending = set(processing.framework.modules())
        # add a node for each tag
        for tag in tags:
            tagNode = Panel.TagItem(topNode, tag)
            # and its children
            #, sorted alphabetically
            modules = sorted(processing.framework.modulesByTag(tag),
                key=lambda x: x.name())
            for mod in modules:
                modNode = Panel.ModuleItem(mod)
                tagNode.addChild(modNode)
                pending.discard(mod)
        # add non-tagged modules
        tagNode = Panel.TagItem(topNode)
        for mod in sorted(pending, key=lambda x: x.name()):
            modNode = Panel.ModuleItem(mod)
            tagNode.addChild(modNode)
    def onItemActivated(self, item, _):
        """ This slot pops up the relevant dialog. """
        if type(item) is Panel.ModuleItem:
            dialog = Dialog(self._iface, item.module())
            self._dialogs.append(dialog)
            dialog.show()

class Dialog(View):
    def __init__(self, iface, module):
        self._module = module
        self._moduleinstance = module().instance()
        View.__init__(self, label = self.module().name())
    def module(self):
        return self._module
    def show(self):
        self._moduleinstance.configure_traits(view = self)
        

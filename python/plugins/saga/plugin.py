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

import os
import processing
import processing.parameters
import saga_api as saga

def getLibraryPaths():
    try:
        paths = os.environ['MLB_PATH'].split(':')
    except KeyError:
        paths = ['/usr/lib/saga/', '/usr/local/lib/saga/']
        print "MLB_PATH not set."
    for p in paths:
        #print "Seaching SAGA modules in " + p + "."
        if os.path.exists(p):
            return [p + '/' + fn for fn in os.listdir(p)]
    raise RuntimeError("No SAGA modules found.")

class SAGAPlugin:
    def __init__(self, _):
        self.libraries = list()
        self._modules = None
        for p in getLibraryPaths():
            try:
                self.libraries.append(Library(p))
            except InvalidLibrary:
                pass
    def initGui(self):
        pass
    def unload(self):
        pass

class InvalidLibrary(RuntimeError):
    def __init__(self, name):
        RuntimeError.__init__(self, "Library invalid " + name + ".")
        
class Library:
    def __init__(self, filename):
        self.sagalib = saga.CSG_Module_Library(saga.CSG_String(filename))
        if not self.sagalib.is_Valid():
            raise InvalidLibrary(filename)
        self._modules = None
        processing.framework.registerModuleProvider(self)
    def modules(self):
        if self._modules is not None:
            return self._modules
        self._modules = set()
        for i in range(self.sagalib.Get_Count()):
            try:
                self._modules.add(Module(self.sagalib, i))
            except InvalidModule:
                pass
        return self._modules

class InvalidModule(RuntimeError):
    def __init__(self, name):
        RuntimeError.__init__(self, "Module invalid " + name + ".")
            
class Module(processing.Module):
    def __init__(self, lib, i):
        self.module = lib.Get_Module(i)
        if not self.module:
            raise InvalidModule("#" + str(i))
        self.interactive = self.module.is_Interactive()
        self.grid = self.module.is_Grid()
        if self.interactive and self.grid:
            self.module = lib.Get_Module_Grid_I(i)
        elif self.grid:
            self.module = lib.Get_Module_Grid(i)
        elif self.interactive:
            self.module = lib.Get_Module_I(i)
        self._parameters = None
        processing.Module.__init__(self,
            self.module.Get_Name(),
            self.module.Get_Description())
    def addParameter(self, sagaParam):
        from processing.parameters import *
        sagaToQGisParam = {
            #saga.PARAMETER_TYPE_Node:   ParameterList,
            saga.PARAMETER_TYPE_Int:    NumericParameter,
            saga.PARAMETER_TYPE_Double: NumericParameter,
            saga.PARAMETER_TYPE_Degree: NumericParameter,
            saga.PARAMETER_TYPE_Bool:   BooleanParameter,
            saga.PARAMETER_TYPE_String: StringParameter,
            saga.PARAMETER_TYPE_Text:   StringParameter,
            saga.PARAMETER_TYPE_FilePath: PathParameter,
            saga.PARAMETER_TYPE_Choice: ChoiceParameter
        }
        name = sagaParam.Get_Name()
        descr = sagaParam.Get_Description()
        typ = sagaParam.Get_Type()
        try:
            qgisParam = sagaToQGisParam[typ]
            if typ == saga.PARAMETER_TYPE_Choice:
                qgisParam.setChoices(["a", "b", "c"])
            self._parameters.add(qgisParam(name, descr))
        except KeyError:
            self._parameters.add(Parameter(name, descr, str))
    def parameters(self):
        if self._parameters is not None:
            return self._parameters
        self._parameters = set()
        for i in range(self.module.Get_Parameters_Count()):
            params = self.module.Get_Parameters(i)
            for j in range(params.Get_Count()):
                self.addParameter(params.Get_Parameter(j))
        return self._parameters
    def tags(self):
        return processing.Module.tags(self) | set([processing.Tag('saga')])



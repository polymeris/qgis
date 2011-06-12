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
        print "Seaching SAGA modules in " + p + "."
        if os.path.exists(p):
            return [p + '/' + fn for fn in os.listdir(p)]
    raise RuntimeError("No SAGA modules found.")

class SAGAPlugin(processing.Plugin):
    def __init__(self, iface):
        libraries = list()
        for p in getLibraryPaths():
            try:
                libraries.append(Library(p))
            except InvalidLibrary:
                #print "Invalid library."
                pass
        processing.Plugin.__init__(self, iface, libraries)

class InvalidLibrary(RuntimeError):
    def __init__(self, name):
        RuntimeError.__init__(self, "Library invalid " + name + ".")
        
class Library(processing.Library):
    def __init__(self, filename):
        #print filename
        lib = saga.CSG_Module_Library(saga.CSG_String(filename))
        if not lib.is_Valid():
            raise InvalidLibrary(filename)
        modules = list()
        for i in range(lib.Get_Count()):
            try:
                modules.append(Module(lib, i))
            except InvalidModule:
                #print "Invalid module."
                pass
        processing.Library.__init__(self,
            lib.Get_Name().c_str(), lib.Get_Description().c_str(),
            modules)

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
        processing.Module.__init__(self,
            self.module.Get_Name(),
            self.module.Get_Description())

        for i in range(self.module.Get_Parameters_Count()):
            params = self.module.Get_Parameters(i)
            #print params.Get_Name() + " - " + params.Get_Identifier()
            for j in range(params.Get_Count()):
                self.addParameter(params.Get_Parameter(j))
    def addParameter(self, sagaParam):
        sagaToQGisParam = {
            saga.PARAMETER_TYPE_Int:
                processing.parameters.NumericParameter,
            saga.PARAMETER_TYPE_Double:
                processing.parameters.NumericParameter,
            saga.PARAMETER_TYPE_Degree:
                processing.parameters.NumericParameter
        }
        name = sagaParam.Get_Name()
        descr = sagaParam.Get_Description()
        typ = sagaParam.Get_Type()
        try:
            qgisParam = sagaToQGisParam[typ]
            self._parameters.add(qgisParam(name, descr))
            #print "Added parameter " + name
        except KeyError:
            #print name + " is of unhandled parameter type."
            pass
    def parameters(self):
        print self._parameters
        return self._parameters
    def tags(self):
        return processing.Module.tags(self) | set([processing.Tag('saga')])



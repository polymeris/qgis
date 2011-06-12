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
import otbApplication as otb
        
class OTBLibrary(processing.Library):
    def __init__(self, modulename):
        lib = modulename
        modules = list()
        modules.append(OTBModule(modulename))
        processing.Library.__init__(self, modulename, modulename,
            modules)

class OTBPlugin(processing.Plugin):
    def __init__(self, iface):
        libraries = otb.Registry.GetAvailableApplications()
        libs = list()
        for p in libraries:
            try:
                libs.append(OTBLibrary(p))
            except InvalidLibrary:
                #print "Invalid library."
                pass
        processing.Plugin.__init__(self, iface, libs)

class InvalidModule(RuntimeError):
    def __init__(self, name):
        RuntimeError.__init__(self, "Module invalid " + name + ".")
        
class OTBModule(processing.Module):
    def __init__(self, modulename):
        self.app = otb.Registry.CreateApplication(modulename)
        processing.Module.__init__(self,
            self.app.GetName(),
            self.app.GetDescription())

        for p in self.app.GetParametersKeys():
            self.addParameter(p)

    def addParameter(self, otbParamKey):
        otbToQGisParam = {
            otb.ParameterType_Int:
                processing.parameters.NumericParameter,
        }
        
        name = otbParamKey
        descr = self.app.GetParameterName(otbParamKey)
        typ = self.app.GetParameterType(otbParamKey)
        try:
            qgisParam = otbToQGisParam[typ]
            self._parameters.add(qgisParam(name, descr))
        except KeyError:
            #print name + " is of unhandled parameter type."
            pass
    def parameters(self):
        return self._parameters
    def tags(self):
        return processing.Module.tags(self) | set([processing.Tag('otb')])



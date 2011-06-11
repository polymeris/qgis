# -*- coding: utf-8 -*-

#	QGIS Processing Framework
#
#	moduleinstance.py (C) Camilo Polymeris
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

import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore

class ModuleInstance:
    def __init__(self, module):
        self._module = module
        self._parameters = dict(
            [(p, p.defaultValue()) for p in self.module().parameters()])
        self.value = self.__getitem__
        self.setValue = self.__setitem__
    def module(self):
        return self._module
    def parameters(self):
        return self._parameters
    def __getitem__(self, key):
        return self._parameters[key]
    def __setitem__(self, key, value):
        validator = key.validator()
        if validator is not None:
            state, _ = validator.validate(str(value), 0)
            if state != QtGui.QValidator.Acceptable:
                return
        self.emit(PYSIGNAL("valueChanged"), (key, value))
        self._parameters[key] = value

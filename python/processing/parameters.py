# -*- coding: utf-8 -*-

#	QGIS Processing Framework
#
#	parameters.py (C) Camilo Polymeris
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

class Parameter:
    class Role:
        input, output, option, feedback = 1, 2, 3, 4
    class UserLevel:
        basic, advanced = 1, 2
    def __init__(self, name, pType, description = None,
                 defaultValue = None, role = None):
        self._name = name
        self._description = description
        self._type = pType
        self._defaultValue = defaultValue
        self._role = role
    def name(self):
        return self._name
    def description(self):
        return self._description
    def type(self):
        return self._type
    def role(self):
        return self._role
    def userLevel(self):
        return UserLevel.basic
    def isMandatory(self):
        return False
    def defaultValue(self):
        if self._defaultValue is not None:
            return self._defaultValue
        try:
            return self.type()()
        except:
            return ""
    def validator(self):
        return None

class ParameterList(Parameter):
    def __init__(self, name, description = None,
				 defaultValue = [], role = None):
        Parameter.__init__(self, name, list, description,
				 defaultValue, role)
                 
class NumericParameter(Parameter):
    def __init__(self, name, description = None,
				 defaultValue = 0.0, role = None):
        Parameter.__init__(self, name, float, description,
				 defaultValue, role)

class BooleanParameter(Parameter):
    def __init__(self, name, description = None,
				 defaultValue = False, role = None):
        Parameter.__init__(self, name, bool, description,
				 defaultValue, role)

class ChoiceParameter(Parameter):
    def __init__(self, name, description = None,
				 defaultValue = -1, role = None, choices = []):
        Parameter.__init__(self, name, int, description,
            defaultValue, role)
        self._choices = choices
    def setChoices(self, choices):
        self._choices = choices
    def choices(self):
        return self._choices

class StringParameter(Parameter):
    def __init__(self, name, description = None,
				 defaultValue = "", role = None):
        Parameter.__init__(self, name, int, description,
				 defaultValue, role)
            
class PathParameter(StringParameter):
    def __init__(self, name, description = None,
				 defaultValue = ".", role = None):
        StringParameter.__init__(self, name, description,
				 defaultValue, role)
                 
Validator = QtGui.QValidator

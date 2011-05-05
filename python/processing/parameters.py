class Parameter:
	class Role:
		input, output, option, feedback = 1, 2, 3, 4
	class UserLevel:
		basic, advanced = 1, 2
	def __init__(self, name, pType, description = None,
				 defaultValue = None, role = None):
		self.name = name
		self.description = description
		self.pType = pType
		self.defaultValue = defaultValue
		self.role = role
	def name(self):
		return self.name
	def description(self):
		return self.description
	def type(self):
		return self.pType
	def role(self):
		return self.role
	def userLevel(self):
		return UserLevel.basic
	def isMandatory(self):
		return False
	def defaultValue(self):
		if self.default is not None:
			return self.default
		else:
			return self.type()()

import PyQt4.QtGui as QtGui

Validator = QtGui.QValidator

# -*- coding: utf-8 -*-

'''
class Test(object):
	__name = "peter"
	
	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, name):
		self.__name = name
		return self.__name
'''

class Test(object):
	__name = "ken"
	
	def getName(self):
		return self.__name
	
	def setName(self, name):
		self.__name = name
		return self.__name
		
	name = property(getName, setName)
	
obj1 = Test()
print(obj1.name)
obj1.name = "bbbbbbbbbbbbb"
print(obj1.name)
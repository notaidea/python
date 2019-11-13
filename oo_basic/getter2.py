# -*- coding: utf-8 -*-

class Test(object):
	def __init__(self):
		self.__num = 222

	@property
	def num(self):
		return self.__num

	@num.setter
	def num(self, num):
		self.__num = num

obj1 = Test()
print(obj1.num)
obj1.num = 333
print(obj1.num)
# -*- coding: utf-8 -*-

class Test(object):
	def __init__(self):
		self.__num = 100
	
	#方法名没规定
	#推荐用get开头
	def getNum(self):
		return self.__num
	
	#方法名没规定
	#推荐用set开头	
	def setNum(self, num):
		self.__num = num
	
	#这是其中一种方法
	num = property(getNum, setNum)
	
obj1 = Test()
print(obj1.num)
obj1.num = 222
print(obj1.num)
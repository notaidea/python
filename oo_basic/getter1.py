# -*- coding: utf-8 -*-

class Test1(object):
	def __init__(self):
		self.__num = 111
	
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

#==================================================
class Test2(object):
	def __init__(self):
		self.__num = 222

	@property
	def num(self):
		return self.__num

	@num.setter
	def num(self, num):
		self.__num = num

obj1 = Test1()
print(obj1.num)
obj1.num = 1111
print(obj1.num)

print("*" * 50)
#==================================================
obj1 = Test2()
print(obj1.num)
obj1.num = 2222
print(obj1.num)

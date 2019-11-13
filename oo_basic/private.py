# -*- coding: utf-8 -*-

'''
python本质上并不完全支持私有化，只不过是将名字进行改变了
'''

class Test(object):
	__num = 0

	def __init__(self):
		self.__num = 100

	def setNum(self, num):
		self.__num = num

	def getNum(self):
		return self.__num

obj1 = Test()

'''
#直接访问是不行的
print(obj1.__num)

#这样可以访问，因为这样是动态添加属性
#要想完全私有化，可以配合__slots__
obj1.__num = 200
print(obj1.__num)

#这样也可以访问
#要想完全私有化，可以配合__slots__
print(obj1._Test__num)
'''

#加上getter和setter后
print(obj1.getNum())


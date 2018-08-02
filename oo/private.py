# -*- coding: utf-8 -*-

class Foo(object):
	#name = "peter"
	__name = "peter"
	
	def __say(self):
		print("__say")
	
	def say(self):
		self.__say()
		
obj1 = Foo()
#print(obj1.name)
#print(obj1.__name)

'''
因为python是动态语言
可以动态添加属性
动态添加一个和私有属性名一样的属性，会覆盖掉原来的私有属性
'''
obj1.__name = "qqqq"
print(obj1.__name)

#obj1.__say()
obj1.say()
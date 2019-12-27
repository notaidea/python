# -*- coding: utf-8 -*-

"""
类装饰器
用类去装饰一个函数

构造函数传入回调方法
__call__执行
"""

class Test(object):
	def __init__(self, func):
		self.__func = func

	def __call__(self):
		print("aaaaaaaaaaaaa")
		self.__func()

	def say(self):
		print("bbbbbbbbbbbbb")

@Test
def test1():
	print("---test-----")

def test2():
	print("---test-----")

#obj1 = Test()
#obj1()

test1()

"""
不用@
"""
t = Test(test2)
t()
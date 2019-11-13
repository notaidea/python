# -*- coding: utf-8 -*-

class Test(object):
	def say(self):
		print("this is Parent")
		
class Child(Test):
	def say(self):		
		#第一个参数是自己的类名
		super(Child, self).say()
		
		#也可以这样简写
		#super().say()
		
		print("this is child")
		
obj1 = Child()
obj1.say()
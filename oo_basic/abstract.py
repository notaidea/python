# -*- coding: utf-8 -*-

'''
python中没有interface这一说法，
要用抽象类或第三方来模拟
'''
from abc import ABCMeta, abstractmethod, abstractproperty

class Test(metaclass = ABCMeta):
	@abstractmethod
	def say(self):
		pass

class Child(Test):
	def go(self):
		print("gogogogo")
	
	def say(self):
		print("pro")
		
obj1 = Child()
obj1.go()

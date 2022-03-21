# -*- coding: utf-8 -*-

"""
支持多重继承
"""
class Parent1(object):
	def say(self):
		print("Parent1")
	
class Parent2(object):
	def info(self):
		print("Parent2")

class Test(Parent1, Parent2):
	pass

obj1 = Test()
obj1.say()
obj1.info()
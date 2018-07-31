# -*- coding: utf-8 -*-

class Test(object):
	def __init__(self):
		self.name = "peter"
		self.age = 10
	
	def __getattribute__(self, obj):
		print("getting attr:")
		print(obj)

obj1 = Test()
obj1.name
obj1.age
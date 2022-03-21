# -*- coding: utf-8 -*-

class Test(object):
	@classmethod
	def say(self):
		print("saying......")
	
	"""
	@staticmethod，表示这是个静态方法，不会自动传入形参self
	"""
	@staticmethod
	def go():
		print("gogogo......")
		
obj1 = Test()
#Test.say()
Test.go()
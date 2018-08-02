# -*- coding: utf-8 -*-

class Test(object):
	def say(self):
		print("saying......")
	
	@staticmethod
	def go():
		print("gogogo......")
		
obj1 = Test()
#Test.say()
Test.go()
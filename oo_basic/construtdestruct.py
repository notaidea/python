# -*- coding: utf-8 -*-

class Test(object):
	def __init__(self):
		print("init......")
		
	def __del__(self):
		print("destruct......")
		
obj1 = Test()

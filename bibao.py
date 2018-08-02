# -*- coding: utf-8 -*-

def check(func):
	def _check(num):
		print("checking......")
		func(num)
		
	return _check
	
@check
def run(num):
	print("num is %d"%(num))
	
run(1)
run(2)
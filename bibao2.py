# -*- coding: utf-8 -*-

def check(str1):
	print("input is %s\n"%(str1))
	
	def _check1(func):	
		def _check2(*args, **kwargs):
			print("checking......")
			func(*args, **kwargs)
		return _check2
	return _check1
	
@check("aaaaaaaaaaaaaaa")
def run(num):
	print("num is %d"%(num))
	
run(1)
run(2)
run(3)
	
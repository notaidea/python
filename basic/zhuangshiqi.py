# -*- coding: utf-8 -*-

"""
装饰器
"""
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

"""
不使用语法糖的情况下
"""
print("=" * 100)
art1 = check(run)
art1(3)
art1(4)

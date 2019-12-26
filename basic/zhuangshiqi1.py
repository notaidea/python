# -*- coding: utf-8 -*-

"""
装饰器什么时候进行装饰
不能在函数运行时进行装饰，只能在函数定义时进行装饰
只要python解释器执行到了这个代码，那么就会自动的进行装饰，而不是等到调用才装饰
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

# -*- coding: utf-8 -*-

def test1():
	for i in range(5):
		print("-----%d-----"%(i))
		yield i

"""
#用__next__()的话，要用try-except包起来
t1 = test1()
try:
	t1.__next__()
	t1.__next__()
	t1.__next__()
	t1.__next__()
	t1.__next__()
	t1.__next__()
	t1.__next__()
	t1.__next__()
	t1.__next__()
	t1.__next__()
	t1.__next__()
	t1.__next__()
	t1.__next__()
	t1.__next__()
	t1.__next__()
	t1.__next__()
	t1.__next__()
except Exception:
	pass
"""

"""
#for循环迭代
for i in test1():
	pass
"""

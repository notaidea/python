# -*- coding: utf-8 -*-

def test1():
	for i in range(10):
		temp = yield i
		if temp == "haha":
			print("%d --- %s"%(i, temp))

"""
send()
	next()跟send()不同的地方是，next()只能以None作为参数传递，而send()可以传递yield的值
	不能用于__next__()之前，也不能单独使用
	必须要传参数，没参数可以传个None,参数是传到yield的
"""
t = test1()
t.__next__()
t.__next__()
t.__next__()

t.send("haha")

t.__next__()
t.__next__()
t.__next__()

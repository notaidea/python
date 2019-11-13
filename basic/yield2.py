# -*- coding: utf-8 -*-

def test1():
	for i in range(10):
		print("-----%d-----"%(i))
		yield i

'''		
t1 = test1()	
t1.__next__()
t1.__next__()
t1.__next__()
'''

for i in test1():
	pass
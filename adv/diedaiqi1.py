# -*- coding: utf-8 -*-

list1 = [11, 22, 33, 44, 55]

"""
判断是否可迭代
"""
from collections import Iterable
print(isinstance(list1, Iterable))
print(isinstance(10, Iterable))
print(isinstance("aaa", Iterable))

"""
"""
for i in list1:
	print(i)
	
print("="*50)

it = iter(list1)
while True:
	try :
		#print(it.__next__())
		print(next(it))
	except Exception:
		break

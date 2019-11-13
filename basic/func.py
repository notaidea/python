# -*- coding: utf-8 -*-

str1 = "hello"
'''
def test():
	str1 = "aaaaa"
	print(str1)
'''

def test():
	global str1
	str1 = "bbbbb"
	print(str1)

test()
print(str1)
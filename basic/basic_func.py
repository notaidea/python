# -*- coding: utf-8 -*-

"""
lambda
"""
sum1 = lambda x,y : x + y
print(sum1(1, 2))
print("=" * 100)

"""
有限参数
"""
def hello1(a, b = 2):
    print(a, end = "")
    print(" === ", end = "")
    print(b)

hello1(1)
hello1(1, 2)
print("=" * 100)

"""
不定长参数
"""
def hello2(*args):
    print(args)

hello2(1)
hello2(1, 2)
hello2(1, 2, 3)
print("=" * 100)

"""
关键字参数
"""
def hello3(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

hello3("J",33,city = "Beaijing",job = "Engineer")
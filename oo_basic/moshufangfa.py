# -*- coding: utf-8 -*-

"""
__str__
类似于php的__toString()
用于返回 print()一个类时的信息

__repr__
类似于__str__，只是__repr__用于交互式命令行时候(ironpython)
如果没有定义返回值则返回内存地址
"""
class Obj1(object):
    #构造函数
    def __init__(self):
        print("init......")
        self.name = "peter"
        self.age = 10

    def __del__(self):
        print("destruct......")

    def __str__(self):
        return "aaaaa"

    def __repr__(self):
        return "bbbbb"

    def __getattribute__(self, obj):
        print("getting attr:")
        print(obj)

obj = Obj1()
print(obj)
obj.name
obj.age

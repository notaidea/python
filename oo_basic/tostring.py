# -*- coding: utf-8 -*-

"""
__repr__
类似于php的__toString()
用于返回 print()一个类时的信息
"""
class Obj1:
    name = "peter"

    def __repr__(self):
        return  "aaaaaaaaaaa"

obj = Obj1()
print(obj)
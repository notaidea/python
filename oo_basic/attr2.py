# -*- coding: utf-8 -*-

"""
__slots__
    __slots__里定义里的，不能和属性冲突
    只能访问和设置__slots__里定义的属性
"""
class Obj1:
    __slots__ = ("name", )

obj = Obj1()
obj.name = "ken"
print(obj.name)

obj.age = 10
print(obj.age)

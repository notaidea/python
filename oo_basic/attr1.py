# -*- coding: utf-8 -*-

from types import MethodType

"""
可以动态添加属性和方法
"""
class Obj1:
    name = "peter"

obj = Obj1()
print(obj.name)
obj.age = 10
print(obj.age)

def run(self):
    print(self)

obj.run = MethodType(run, obj)
obj.run()
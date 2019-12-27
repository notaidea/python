# -*- coding: utf-8 -*-

from types import MethodType

"""
可以动态添加属性和方法
"""
class Person(object):
    name = "peter"

#类动态添加属性
Person.addr = "深圳"

obj1 = Person()
obj1.age = 10

print(obj1.name)
print(obj1.age)
print(obj1.addr)

def run(self):
    print(self)

obj1.run = MethodType(run, obj1)
obj1.run()

obj2 = Person()
print(obj2.addr)

# -*- coding: utf-8 -*-

from types import MethodType

"""
1、定义字段
2、__init__内动态增加字段
3、类动态添加属性
"""
class Person(object):
    #定义字段
    name = "peter"

    def __init__(self, age):
        self.age = age

#类动态添加属性
Person.school = "深圳中心"

obj1 = Person(10)

print(obj1.name)
print(obj1.age)
print(obj1.school)

def run(self):
    print(self)

obj1.run = MethodType(run, obj1)
obj1.run()

obj2 = Person(20)
print(obj2.school)

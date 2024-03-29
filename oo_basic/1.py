# -*- coding: utf-8 -*-

"""
==================================================
继承
class Person(object)，继承自object
    object自带很多拦截器（__getattribute__、__setattr__等）

元类
==================================================
"""
class Person(object):
    """
    ==================================================
    元信息，对象被调用时就会调用
    ==================================================
    """
    print("aaaaaaaaaa")

    num = 10
    if num > 0:
        print("bbbbbbbbbb")

p = Person()
print("=" * 100)

"""
==================================================
创建对象的方法
类()创建
type()创建
==================================================
"""
class Test1(object):
    def say(self):
        print("test1")

obj1 = Test1()
obj1.say()

def hello(self):
    print("hello - " + self.name)

"""
==================================================
type(类名， 继承自谁()， 绑定方法和属性{})
==================================================
"""
Test2 = type("Test2", (Test1, ), {"hello": hello, "name" : "peter"})
obj2 = Test2()
obj2.say()
obj2.hello()

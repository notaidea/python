# -*- coding: utf-8 -*-

"""
元类
"""
class Person(object):
    """
    元信息，对象被调用时就会调用
    """
    print("aaaaaaaaaaaaaaaaaaaa")

    num = 10
    if num > 0:
        print("aaaaaaaa")

p = Person()

"""
创建对象的方法
class关键字创建
type()创建
"""
class Test1(object):
    def say(self):
        print("test1")

obj1 = Test1()
obj1.say()

def hello(self):
    print("hello - " + self.name)

#type(类名， 继承自谁()， 绑定方法和属性{})
Test2 = type("Test2", (Test1, ), {"hello": hello, "name" : "peter"})
obj2 = Test2()
obj2.say()
obj2.hello()


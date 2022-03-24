# -*- coding: utf-8 -*-

"""
装饰器用在类方法上（非静态）
内部的function，第一个形参对应类方法的self

装饰器用在类静态方法上
不能和非静态方法共用装饰器（形参个数不一样）
@staticmethod要写在最上面
"""
def check(func):
    #第一个形参对应类方法的self
    def _check(obj):
        print("checking......")

        func(obj)
    
    return _check

def checkstatic(func):
    #第一个形参对应类方法的self
    def _check():
        print("checking......")

        func()
    
    return _check

class Test():
    def __init__(self, name):
        self.name = name

    @check
    def say(self):
        print(self.name)

    #@staticmethod要写在最上面
    @staticmethod
    @checkstatic
    def info():
        print("info")

obj = Test("peter")
obj.say()
Test.info()

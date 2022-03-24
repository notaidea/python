# -*- coding: utf-8 -*-

"""
对象装饰器，必须实现：
    def __init__(self, func):
    def __call__(self, *args, **kwargs):

对象装饰器只能用在对象、静态方法、函数上（不能是类方法，因为形参self无法传入）
"""
class Checker(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("checking")
        return self.func(*args, **kwargs)

class Test(object):
    def __init__(self, name):
        self.name = name

    #@Checker
    def say(self):
        print(self.name)

    @staticmethod
    @Checker
    def info():
        print("info")

obj = Test("peter")
obj.say()
Test.info()

"""
作用在对象上的对象装饰器
"""
class singleton:
    def __init__(self,func):
        self.func = func
        self.instance = None
    
    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.func(*args, **kwargs)
        return self.instance

@singleton
class Article(object):

    def __init__(self):
        pass

art1 = Article()
art2 = Article()

#
print("判断是否单例，测试时可以把'@singleton'给注释掉:")
print(art1 == art2)
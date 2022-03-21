# -*- coding: utf-8 -*-

"""
装饰器
    带输入参数，装饰器外面再包裹一层函数
"""

#最外层的装饰器用来接收输入参数
def checkLogin(input1):
    #第二层的装饰器用来接收输入函数
    def check(func):
        def inner():
            func()
        return inner
    return check

@checkLogin("aaa")
def create():
    print("creating!!!!!")

create()

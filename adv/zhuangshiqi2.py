# -*- coding: utf-8 -*-
"""
多个装饰器
    多个装饰器运行过程类似于递归
    离函数名最近的会先装饰，但是不执行装饰器里的回调函数,再次检查有没别的装饰器
    检查完后，再倒序执行回调函数
"""
def checkLogin(func):
    print("正在装饰---checkLogin")

    def _check():
        print("checkLogin")
        func()

    return _check

def checkAuth(func):
    print("正在装饰---checkAuth")

    def _check():
        print("checkAuth")
        func()

    return _check

@checkLogin
@checkAuth
def create():
    print("creating")

create()

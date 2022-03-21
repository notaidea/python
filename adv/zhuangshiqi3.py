# -*- coding: utf-8 -*-

"""
装饰器
    有参函数
    带返回值
"""
def checkLogin(func):
    """
    def inner(input1 = ""):
        func(input1)
    """
    def inner(*args, **kwargs):
        #return func(*args, **kwargs) 这样在外部能接收到原函数的返回值

        func(*args, **kwargs)

        #这样return的话，原函数的返回值无法接收
        return "qqqqqqqq"

    return inner

@checkLogin
def create(input1 = "", input2 = ""):
    print("creating 1 --- " + input1)
    print("creating 2 --- " + input2)
    return "1234"

"""
res收到的返回值是装饰器的返回值
create()被装饰后，就不指向自己了，而是指向了装饰器
想要返回create()的返回值的话，直接在装饰器内返回函数 return func(*args, **kwargs) 
"""
res = create("hello", "world")
print(res)

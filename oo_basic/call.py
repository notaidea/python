# -*- coding: utf-8 -*-

class Test1(object):
    
    """
    ==================================================
    类似php的__invoke()

    __call__的参数是不固定的
    ==================================================
    """
    #def __call__(self, arg1, arg2, arg3):
    def __call__(self, *arg1):
        print(arg1)

obj1 = Test1()
obj1("aaaaa", "bbbbb")

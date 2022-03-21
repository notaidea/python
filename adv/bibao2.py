# -*- coding: utf-8 -*-

def counter():
    #这里要用数组，因为数组是引用的
    cnt = [0]

    def _counter():
        cnt[0] = cnt[0] + 1
        return cnt[0]
    
    return _counter

c = counter()
print(c())
print(c())

# -*- coding : utf-8 -*-

"""
实现深拷贝
"""
import copy
a = [11, 22, 33]
b = copy.deepcopy(a)

print(id(a))
print(id(b))

a.append(44)

print(id(a))
print(id(b))

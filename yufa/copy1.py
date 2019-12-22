# -*- coding : utf-8 -*-
"""
练习时用list

浅拷贝:仅仅是复制了引用

深拷贝:完全复制
"""

a = [11, 22, 33]
b = a

print(id(a))
print(id(b))

a.append(44)

print(id(a))
print(id(b))

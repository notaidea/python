# -*- coding: utf-8 -*-

turple1 = ("aa", "bb", "cc")
turple2 = "dd", "ee"
turple3 = "ff", #不加最后的","，就是个字符串

print(turple1)
print(turple2)
print(turple3)
print(turple1.index("aa"))

"""
下标访问
"""
print(turple1[0])
print(turple1[1])

"""
运算符操作
"""
print(turple1 + turple2)

"""
遍历
"""
for i in turple1:
    print(i)

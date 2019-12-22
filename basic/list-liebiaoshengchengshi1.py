# -*- coding:utf-8 -*-

"""
生成一个列表
"""
list1 = range(0, 10)
print(list1)

list2 = [i for i in range(0, 10)]
print(list2)

#带条件的
list3 = [i for i in range(0, 10) if i % 2 == 0]
print(list3)

#双层for循环
list4 = [(i, j) for i in range(0, 5) for j in range(0, 5)]
print(list4)

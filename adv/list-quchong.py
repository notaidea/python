# -*- coding : utf-8 -*-

"""
列表去重
"""
list1 = [1, 1, 2]
print(list1)

#去重，并转换回列表
list2 = set(list1)
list2 = list(list2)
print(list2)

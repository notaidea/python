# -*- coding: utf-8 -*-

import os

"""
fh返回的是个流
如果你先读了2个字符：fh.read(2)
再读2个字符的话，就会从上次已读取的地方开始读
"""
fh = open('./test1.txt', "r")

# 读n个字符
# print(fh.read(2))

# 读n行，默认1行，返回str，需要和循环配合
# print(fh.readline())

# 读n行，默认1行，返回arr，需要和循环配合
# print(fh.readlines(3))

while True:
    res = fh.readline()

    if res == "":
        break

    print(res.strip("\n"))

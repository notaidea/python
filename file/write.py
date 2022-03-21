# -*- coding: utf-8 -*-

fh = open("./test1.txt", "w")
fh.write("aaa\n")

"""
写入多行
传入字符数组或可迭代对象
"""
fh.writelines(["bbb\n", "ccc\n"])

# -*- coding: utf-8 -*-

from hashlib import md5
import hashlib


str1 = " hello, "
str2 = "world"
str3 = str1 + str2

#多行输入
str4 = """
aaaaa
bbbbb
ccccc
"""

print(str3)
print(str4)

print(str1[::-1])
print(str1[0:3])
print(str1.strip())
print(str1.upper())
print(len(str1))
print(str1.find("ll"))
print(str1.replace("l", "L"))
print("%d - %s"%(0, "aaa"))

"""
md5
"""
str4 = "hello,world."
md5 = hashlib.md5()
#md5.update(b"hello,world.")
md5.update(str4.encode("UTF-8"))
md5_res = md5.hexdigest()
print(md5_res)

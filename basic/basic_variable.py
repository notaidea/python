# -*- coding: utf-8 -*-

"""
作用域是局部的
"""
num1 = 10
str1 = "hello"
arr1 = ["aa", "bb"]
dict1 = {"name" : "peter"}
turple1 = ("c", "d")

def hello1():
    #加上这个，设为全局作用域
    #global num1
    num1 = 20

hello1()
print(num1)
print("=" * 100)

"""
查看变量类型
"""
print(type(num1))
print(type(str1))
print(type(arr1))
print(type(dict1))
print(type(turple1))

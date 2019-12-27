# -*- coding: utf-8 -*-

"""
__dir__
列出对象的所有属性（方法）名
"""
class Obj1:
    name = "peter"

    def run(self):
        print("running!")

obj = Obj1()
print(obj.__dir__())

print("=" * 50)
print(dir(obj))

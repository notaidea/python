# -*- coding: utf-8 -*-

dict1 = {
    "name" : "peter",
    "age" : 10
}

print(dict1)
print(dict.keys)
print(dict.values)
print(len(dict1))

"""
==================================================
下标访问
==================================================
"""
print(dict1["name"])
print(dict1.get("name"))

"""
==================================================
遍历
==================================================
"""
for i in dict1:
    print("%s --- %s"%(i, dict1.get(i)))

"""
遍历（类foreach）
"""
for k, v in dict1.items():
    print("%s --- %s"%(k, v))

"""
==================================================
pop
==================================================
"""
print(dict1.pop("name"))
print(dict1)

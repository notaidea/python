# -*- coding: utf-8 -*-

dict1 = {
    "name" : "peter",
    "age" : 10
}

print(dict1)
print(len(dict1))

"""
下标访问
"""
print(dict1["name"])
print(dict1.get("name"))

#pop
print(dict1.pop("name"))
print(dict1)

"""
遍历
"""
for k, v in dict1.items():
    print("%s - %s"%(k, v))

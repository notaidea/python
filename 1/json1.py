# -*- coding: utf-8 -*-

import json

dict1 = {
    "name": "peter",
    "age": 10
}

"""
其他格式转json字符串，json.dumps(data, ensure_ascii=False)
ensure_ascii=False：解析为中文
"""
json1 = json.dumps(dict1, ensure_ascii=False)
print(json1)
print(type(json1))

"""
json字符串转其他格式
"""
str1 = '{"name": "peter", "age": 10}'
str2 = json.loads(str1)
print(str1)
print(type(str2))

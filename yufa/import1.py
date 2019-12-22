# -*- coding : utf-8 -*-

"""
导入时的搜索路径
"""
import sys

#查看导入时的搜索路径
print(sys.path)

#插入搜索路径
sys.path.append("d:/")
print(sys.path)

#重新导入
#from imp import *
#reload(模块名)
# -*- coding: utf-8 -*-

class Test(object):
	def __init__(self, subject1):
		self.subject1 = subject1
		self.subject2 = "cpp"
	
	'''
	#不能在__getattribute__()再次调用self的属性、方法
	def __getattribute__(self, attrName):
		if attrName.startswith("a"):
			print(attrName)
		else:
			return self.test
	'''
	def __getattribute__(self, attrName):
		if attrName == "subject1":
			return "redirect - __getattribute__"
		else:
			temp = object.__getattribute__(self, attrName)
			return temp

obj1 = Test("python")
print(obj1.subject1)
print(obj1.subject2)

# -*- coding: utf-8 -*-

class Test(object):
	def __init__(self, subject1):
		self.subject1 = subject1
		self.subject2 = "cpp"
	
	'''
	#不能在__getattribute__()再次调用self的属性、方法
	def __getattribute__(self, obj):
		if obj.startswith("a"):
			print(obj)
		else:
			return self.test
	'''
	def __getattribute__(self, obj):
		if obj.startswith("a"):
			return "redirect python"
		else:
			temp = object.__getattribute__(self, obj)
			return temp
			
	def show(self):
		print("hello,world.")

obj1 = Test("python")
print(obj1.subject1)
print(obj1.subject2)
obj1.show()
# -*- coding: utf-8 -*-

'''
python不支持重载
相同的方法名，后面的会覆盖前面的
'''
class Test(object):
	def say(self, num):
		print("11111")
		
	def say(self, num, num2):
		print("22222")
		
obj1 = Test()
#obj1.say(1)
obj1.say(1, 2)

class Test2(Test):
	def say(self, num, num2):
		print("Test2 - say")

print("*" * 100)
obj2 = Test2()
obj2.say(3, 4)

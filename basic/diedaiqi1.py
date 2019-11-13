# -*- coding: utf-8 -*-

list1 = [11, 22, 33, 44, 55]

for i in list1:
	print(i)
	
print("="*50)

it = iter(list1)
while True:
	try :
		#print(it.__next__())
		print(next(it))
	except Exception:
		break
# -*- coding: utf-8 -*-

for i in range(0, 10):
	if i % 2 == 0:
		print("%d %% 2 == 0"%(i))
	elif i % 3 == 0:
		print("%d %% 3 == 0"%(i))
	else :
		print(i)
	
print("="*50)
i = 0	
while True:
	i += 1
	
	if i >= 5:
		break
	
	print(i)
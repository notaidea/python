# -*- coding: utf-8 -*-
num = 0

#raise Exception()
 
try:
	num = 10 / 0
except Exception:
	print("no 0")

print(num)

print("=" * 100)
try:
	num = 10 / 0
except Exception as e:
	print(e)
else:
	print("try ...... else")
finally:
	print("finally ...... else")

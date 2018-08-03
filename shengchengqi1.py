# -*- coding: utf-8 -*-

# 注意这里是()，而不是[]
#gen = (x for x in range(5))

#如果换成[]换成()，那么会成为生成器的表达式。
#gen = [x for x in range(5)]
gen = [x*x for x in range(5) if x >= 2]

for i in gen:
    print(i)
	
print("="*50)


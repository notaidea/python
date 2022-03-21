# -*- coding: utf-8 -*-

a = 0
while True:
    if a > 10:
        break

    a = a + 1
    print(a)

for i in range(0, 5):
    if i % 2 == 0:
        print(i)
    else:
        continue

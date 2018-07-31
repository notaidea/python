# -*- coding: utf-8 -*-

def test(number):
    print("--- 1 ---")

    def test_in(number2):
        print("--- 2 ---", end = '')
        print(number + number2)

    print("--- 3 ---")
    return test_in

sum = test(100)
print("*"*50)
sum(100)
sum(1000)
sum(10000)
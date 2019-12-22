# -*- coding: utf-8 -*-

def test():
    print("---1---")

    def _test1(num):
        print("---2---")
        print(num)

    print("---3---")
    return  _test1

func1 = test()
func1(10)
func1(20)

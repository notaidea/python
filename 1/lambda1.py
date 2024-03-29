a = lambda x,y : x * y
print(a(10, 10))

"""
==================================================
lambda作为形参传入
==================================================
"""
def test(a, b, func):
    result = func(a, b)
    return result


num = test(11, 22, lambda x, y: x + y)
print(num)

#==================================================
#nums = [11,34234,23,344,123,1,23,124,523,4,12342341,423,43545]
#nums.sort()
#print(nums)

infors = [{"name":"laowang","age":10},{"name":"xiaoming","age":20},{"name":"banzhang","age":10}]

infors.sort(key=lambda x:x['age'])

print(infors)

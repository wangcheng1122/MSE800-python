import math

a = [1, 2, 3, 4, 5]


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 计算每个元素的阶乘
factorials = [factorial(x) for x in a]

print(factorials)
factorials = [math.factorial(x) for x in a]
print(factorials)

f = 5
i = 3
# f := f * i
# f *= i
print(f)

number = [1, 2, 3, 4, 5]
factorials = [1 if n == 0 else (f := 1, [f := f * i for i in range(1, n + 1)], f)[-1] for n in number]
print(factorials)

keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
print(dictionary)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

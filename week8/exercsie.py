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

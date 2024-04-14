# Рекурсивана функция - это функция которая внутри себя вызывает себя же

import math


def calc_factorial(num):
    if type(num) is not int:
        raise TypeError("Number must be integer")
    if num <= 0:
        raise ValueError("Number must be positive")
    if num == 1:
        return 1
    return calc_factorial(num - 1) * num


print(calc_factorial(5))
print(math.factorial(5))
# 5! == 5*4*3*2*1 - факториал

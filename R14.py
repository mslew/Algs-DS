from typing import Sequence


def sum_of_squares(n):
    sum = 0
    for i in range(1, n):
        sum = pow(i, 2) + sum 
    return sum
num =  4
print(sum_of_squares(num))
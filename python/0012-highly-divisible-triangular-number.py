# What is the value of the first triangle number to have over five hundred divisors?

from time import time_ns
from math import sqrt

def count_factors(num):
    sum_ = 2 * sum(num % i == 0 for i in range(1, int(sqrt(num)) + 1))
    if int(sqrt(num))**2 == num:
        sum_ -= 1
    return sum_

def triangle_number(n):
    return (n * (n+1)) // 2

def first_with_n_divisors(factors_num):
    i = 1
    while True:
        num = triangle_number(i)
        if count_factors(num) >= factors_num:
            return num
            break
        i += 1

def main():
    start = time_ns()
    print(f"answer: {first_with_n_divisors(500)} in {(time_ns()-start)/1e6}ms")  # 76576500 in 5833.585ms

if __name__ == '__main__':
    main()
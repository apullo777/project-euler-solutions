# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math 

def find_lcm(n):
    lcm = 1
    for i in range(2, n+1):
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm

print(find_lcm(10))



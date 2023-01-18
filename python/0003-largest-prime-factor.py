# What is the largest prime factor of the number 600851475143 ?

import math

def max_prime_factor(n):
    max_prime = -1

    while n % 2 == 0:
        max_prime = 2
        n >>= 1

    # n must be odd at this point
    while n % 3 == 0:
        max_prime = 3
        n /= 3

    # iterate only for integers who does not have prime factor 2 and 3
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        while n % i == 0:
            max_prime = i
            n /= i

        while n % (i+2) == 0:
            max_prime = i + 2
            n /= (i+2)

    if n > 4: max_prime = n

    return int(max_prime)

print(max_prime_factor(600851475143))

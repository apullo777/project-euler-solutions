# What is the 10 001st prime number?

from math import sqrt

def is_prime(n):
    if (n > 1):
        for k in range(2, int(sqrt(n)) + 1):
            if (n % k == 0): 
                return False
        return True
    # If the number is less than 1, its also not a prime number.
    else: 
	    return False

def find_nth_prime(n):
    count, num = 0, 0   
    while (count < n):
        num += 1
        if (is_prime(num)):
            count += 1
    return num

print(find_nth_prime(10001))
# Find the sum of all the primes below two million.

from time import time_ns

def sieve_of_Eratosthenes(n):
    prime = []
    num_list = [True for i in range(n+1)]
    p = 2 
    while (p * p < n):
        # if prime_list[p] is not updated, it is a prime
        if (num_list[p] == True):
            # update all multiples of p as composite    
            for i in range(p * p, n+1, p):
                num_list[i] = False
        p += 1

    for p in range(2, n+1):
        if num_list[p] == True:
            prime.append(p)

    return prime

def main():
    start = time_ns()
    print(f"answer: {sum(sieve_of_Eratosthenes(2000000))} in {(time_ns()-start)/1e6}ms") # 142913828922 in 413.225ms

if __name__ == '__main__':
    main()
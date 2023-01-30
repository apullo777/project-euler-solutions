# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from time import time_ns

def square(n):
    return n * n

def find_triplet_product(sum):
    bound = sum // 3 + 100
    for a in range(1, bound):
        for b in range(1, bound):
            c = (sum - a) - b
            if a < b < c:
                if square(a) + square(b) == square(c):
                    return a * b * c

def main():
    start = time_ns()
    print(f"answer: {find_triplet_product(1000)} in {(time_ns()-start)/1e6}ms") # 31875000 in 36.506ms

if __name__ == '__main__':
    main()
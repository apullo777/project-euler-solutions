def sum_of_multiples(n1, n2, bound):
    return sum(x for x in range(bound) if x % n1 == 0 or x % n2 == 0)

print(sum_of_multiples(3, 5, 1000))
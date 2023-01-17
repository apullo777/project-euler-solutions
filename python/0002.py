# sum of all even-indexed terms of Fibonacci sequence
def sum_of_fibonacci_even_indexed(bound):

    def next_even_item(pre, curr):
        return 2 * curr + pre

    numbers = [2]
    pre, curr = 1, 2
    while next_even_item(pre, curr) < bound:
        new = next_even_item(pre, curr)
        pre, curr = new - curr, new
        numbers.append(curr)

    return sum(numbers)

print(sum_of_fibonacci_even_indexed(4000000))

# sum of all even-valued terms of Fibonacci sequence
def sum_of_fibonacci_even_valued(bound):
    ans = 0
    curr = 1
    nextt = 2
    while curr <= bound:
        if curr % 2 == 0:
            ans += curr
        curr, nextt = nextt, curr + nextt
    return ans

print(sum_of_fibonacci_even_valued(4000000))
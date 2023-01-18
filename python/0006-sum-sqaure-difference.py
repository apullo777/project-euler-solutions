# Find the difference between 
# the sum of the squares of 
# the first one hundred natural numbers 
# and the square of the sum.

def square(n):
    return n * n

def sum_square_difference(n):

    def sum_of_squares():
        return (n * (n+1) * (2*n +1)) // 6

    def square_of_sum():
        return square(((n+1) * n)//2)

    return abs(sum_of_squares() - square_of_sum())


print(sum_square_difference(100))    

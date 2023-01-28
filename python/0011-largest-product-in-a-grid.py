from time import time_ns
import math

input = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

def make_matrix(string, dim):
    # Split the input string into a list of strings
    str_list = string.split(" ")
    
    # Create a 2D grid of the given dimension
    rows = [[] for _ in range(dim)]
    for i in range(dim):
        rows[i] = [int(x) for x in str_list[i*dim : i*dim + dim]]

    # Create a 2D grid of columns
    cols = [[] for _ in range(dim)]
    for i in range(dim):
        cols[i] = [int(x) for x in str_list[i::dim]]
    return rows, cols


def find_largest_product(list, adj_num):
    max_product, curr_product = 0, 1

    # Loop through each sub-list of "num" with length "adj_num"
    for i in range(len(list) - adj_num + 1):
        curr_list = list[i:i + adj_num]

        curr_product = 1

        # Loop through each number in the current list
        for n in curr_list:
            curr_product *= int(n)
        max_product = max(max_product, curr_product)

    return max_product

def get_diagonals(grid, is_bottom_to_top_right=True):
    # Get the number of rows and columns in the grid
    grid_dimension = len(grid)
    # Check if the grid is square
    assert grid_dimension == len(grid[0])
    
    # Initialize an empty list of lists to store the diagonals
    diagonal_grid = [[] for diagonal in range(2 * grid_dimension - 1)]
    
    # Loop through each row and column in the grid
    for row in range(grid_dimension):
        for col in range(grid_dimension):
            # If the flag is_bottom_to_top_right is True, add the item from grid[col][row]
            # to the corresponding diagonal in diagonal_grid
            if is_bottom_to_top_right:
                diagonal_grid[row + col].append(grid[col][row])
            # If the flag is_bottom_to_top_right is False, add the item from grid[row][col]
            # to the corresponding diagonal in diagonal_grid
            else:
                diagonal_grid[col - row + (grid_dimension - 1)].append(grid[row][col])
    
    # Return the list of lists containing the diagonals
    return diagonal_grid



#def compute(input):
#    ans = 0
#    matrix, columns = make_matrix(input, 20)
#    max_diagonal1 = find_largest_product(get_diagonals(matrix, True), 4)
#    max_diagonal2 = find_largest_product(get_diagonals(matrix, False), 4)
#    max_column = find_largest_product(columns, 4)
#    return max(max_diagonal1, max_diagonal2, max_column)

rows = make_matrix(input, 20)[0]
cols = make_matrix(input, 20)[1]

#print(rows)
#print(cols)
#print(get_diagonals(rows, True))
print(get_diagonals(rows, False))
print(type((get_diagonals(rows, False))[0][0]))
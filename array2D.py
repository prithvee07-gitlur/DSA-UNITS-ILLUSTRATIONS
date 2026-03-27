
# ARRAY 2D (MATRIX TRAVERSAL + OPERATIONS)

# PRACTISING 2D ARRAYS FOR REAL-WORLD TABULAR DATA AND UNDERSTAND TRAVERSAL COMPLEXITY.

# 2-D ARRAY : A two-dimensional (2D) array is an array of arrays, organizing data into rows and columns like
#             a table or matrix. Elements are accessed using two indices: one for the row and one for the column.

# ANSWER : 

# defining a function print_matrix taking a matrix as an input 
def print_matrix(matrix):
    for row in matrix: # traversing each row of the matrix

        # map(str,row) : converts numbers from int form to string form in a list [10,12]->['10','12']
        # ' '.join() : connects the string formed in map to string with spaces ('10 20')
        # and printing the final output
        print(' '.join(map(str, row)))  

# defining a new function row_sums taking a matrix as an input
def row_sums(matrix):
    print("\nRow Sums:")

    # looping through the matrix using enumerate
    ''' 
        enumerate(matrix) : is a python built-in function that iterated over a matrix (a list of list), 
        yielding pairs of an index and each row for easy access to row positions. 

        eg :- For matrix = [[1, 2], [3, 4], [5, 6]], the loop for i, row in enumerate(matrix): gives:
        i=0, row=[1, 2]
        i=1, row=[3, 4]
        i=2, row=[5, 6] 
    '''
    for i, row in enumerate(matrix):
        total = sum(row)  # adding all the elements of the row of the matrix
        print(f"Row {i}: {total}")  # printing each row total sum with the row index.

# defining a function columns_sums that will sum the elements of the columns in
# the matrix and takes a matrix as an input
def column_sums(matrix):

    if not matrix or not matrix[0]:  # checking if the matrix is empty 
        print("Empty matrix")
        return
    cols = len(matrix[0])  # counting the number of columns in the matrix

    print("\nColumn Sums:")

    # outer loop : for iterating each columns
    for j in range(cols):
        columns_total=0  # initializing the columns_totals = 0
        for i in range(len(matrix)):  # inner loop : adds all the elements in columns j
            columns_total=columns_total+matrix[i][j]  # adding the cells 
        print(f"Col {j}: {columns_total}")  # printing the total with the column numbers
        
# defining the search_value function for searching values in the matrix that takes 
# matrix and target element as an input
def search_value(matrix, target):
    print(f"\nSearch for {target}:")
    found = False  # initializing the found variable as False

    # looping through the matrix each elements 
    for i in range(len(matrix)): # outer loop - till the length of the matrix
        for j in range(len(matrix[0])):  # inner loop - till the length of the one row of the matrix

            if matrix[i][j] == target: # if element is found
                print(f"Found at position ({i}, {j})")  # printing its position
                found = True # setting the found as True
                return  # Stopping after the first match of the element
            
    if not found: # if element is not found - printing message
        print("Not found")

# defining a function transpose that will calculate the transpose of the matrix
# and takes matrix as an input
def transpose(matrix):

    # checking that the matrix is empty or not
    if not matrix or not matrix[0]:
        print("\nTranspose: Empty")
        return
    
    # calculating the length of rows and cols
    rows, cols = len(matrix), len(matrix[0])

    # Creating an empty transpose matrix 
    trans = [[0] * rows for _ in range(cols)]
    # Filling the elements in it with nested loops
    for j in range(cols):           # Outer loop: create each new row
        for i in range(rows):      # Inner loop: fill each position in that row
            trans[j][i] = matrix[i][j]
        print("\nTranspose Preview:")
        print_matrix(trans) # finally printing the output


# Main demo matrix - testing the above code
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# calling all the functions for testing
print("Original Matrix:")
print_matrix(matrix)

row_sums(matrix)
column_sums(matrix)
search_value(matrix, 7)
transpose(matrix)

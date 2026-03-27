
# ARRAY 1D (OPERATIONS + SHIFTING COST)

# UNDERSTANDING HOW TO INSERT/DELETE IN ARRAYS CAUSES SHIFTING AND IMPACTS COMPLEXITY.

# 1-D ARRAY : A one-dimensional (1D) array is a linear data structure that
#             stores a sequence of elements of the same data type in contiguous memory locations, 
#             accessed using a single index (subscript).

# ANSWER : 

def print_array(arr): # defining a print_array function
    # map(str,arr) : converts numbers from int form to string form in a list [10,12]->['10','12']
    # ' '.join() : connects the string formed in map to string with spaces ('10 20')
    # and printing the final output
    print(' '.join(map(str, arr)))

# making and insert_at function : that will insert an element at a specific index.
# this takes four inputs : arr(current array),pos(0-index to insert at),value(number to add),
# max_capacity(checks overflow of a fixed length array)

def insert_at(arr, pos, value, max_capacity):
    n = len(arr)  # calculating the current length of the array

    # the following if statements checks that whether the length of the array
    # have reached the max capacity or inputted invalid position (negative index) or out of range index.
    if n == max_capacity or pos < 0 or pos > n:  
        print("Insertion not possible")
        return arr, 0   # return the unchanged array
    
    shifts = n - pos  # Exact shift count - calculates how many logical shifts needed
    new_arr = arr[:pos] + [value] + arr[pos:] # creating a new array where we are adding
    # array before pos + value + array after pos.
    return new_arr, shifts # returning new array and no of shifts done.

# making a delete_at function that will delete and element from a specific index 
# it takes two inputs : arr(list),pos(index of element to remove)
def delete_at(arr, pos):
    n = len(arr)  # calculating the current length of an array

    # the following if statements checks that whether the length of the array
    # is zero or inputted invalid position (negative index) or out of range index.
    if n == 0 or pos < 0 or pos >= n:
        print("Deletion not possible")
        return arr, 0   # return the unchanged array
    
    shifts = n - pos - 1  
    # Exact shift count : calculates the number of logical shifts (elements after pos move left)
    new_arr = arr[:pos] + arr[pos+1:]  # creating a new array skipping the element at pos
    return new_arr, shifts  # returning new array and no of shifts done.

# defining a function print_complexity that will print the time complexity
# and takes pos(position), n(length of the array) and is_insert(True for insert, False for delete)
def print_complexity(pos, n, is_insert):

    if is_insert: # if True

        # print O(1) if pos==n and otherwise O(n) due to shifting
        print("Complexity: O(1)" if pos == n else "Complexity: O(n) (shifting)")

    else: # if False

        # print O(1) if pos==n-1 and otherwise O(n) due to shifting
        print("Complexity: O(1)" if pos == n-1 else "Complexity: O(n) (shifting)")

# Main demo - testing the code with an example
arr = [10, 20, 30, 40, 50]
max_capacity = 100
print("Initial array:")
print_array(arr)

# All operations
print("\nInsert START:")
arr, shifts = insert_at(arr, 0, 5, max_capacity)
print("Updated:", end=' ')
print_array(arr)
print(f"Shifts: {shifts}")
print_complexity(0, 5, True)

print("\nInsert MIDDLE:")
arr, shifts = insert_at(arr, len(arr)//2, 99, max_capacity)
print("Updated:", end=' ')
print_array(arr)
print(f"Shifts: {shifts}")
print_complexity(2, 6, True)

print("\nInsert END:")
arr, shifts = insert_at(arr, len(arr), 999, max_capacity)
print("Updated:", end=' ')
print_array(arr)
print(f"Shifts: {shifts}")
print_complexity(6, 7, True)

print("\nDelete START:")
arr, shifts = delete_at(arr, 0)
print("Updated:", end=' ')
print_array(arr)
print(f"Shifts: {shifts}")
print_complexity(0, 7, False)

print("\nDelete END:")
arr, shifts = delete_at(arr, len(arr)-1)
print("Updated:", end=' ')
print_array(arr)
print(f"Shifts: {shifts}")
print_complexity(5, 6, False)

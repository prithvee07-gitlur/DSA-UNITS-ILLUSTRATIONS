
# DYNAMIC ARRAY SIMULATION (RESIZE + POP)

# UNDERSTANDING HOW DYNAMIC ARRAYS GROW AND WHY APPEND IS AMORTIZED O(1).

# DYNAMIC ARRAY : Array that automatically resizes (usually doubles) when full, allowing variable
#                 size unlike fixed arrays. Append is amortized O(1) due to rare resizes.

# ANSWER :

class DynamicArray:  # creating a class - (blueprint)
    def __init__(self):
        self.size = 0        # Number of elements - setting 0
        self.capacity = 4    # Initial capacity - fixing the length
        self.array = [None] * self.capacity  # creating four length empty array
    
    def print_state(self):
        # this only shows the first size elements and ignores unused chairs
        print(f"Size: {self.size}, Capacity: {self.capacity}, Array: {' '.join(map(str, self.array[:self.size]))}")
    
    def append(self, value):
        if self.size == self.capacity:  # when the array is full 
            # RESIZE: Double the capacity of the array
            old = self.array
            self.capacity *= 2 
            self.array = [None] * self.capacity  # creating a bigger array with none
            for i in range(self.size):  # moving all the elements to the new array 
                self.array[i] = old[i]
            print(f"RESIZED: {self.capacity//2} → {self.capacity}")  # printing the message
        
        self.array[self.size] = value # always entering the values to the next empty place available 
        self.size += 1  # increasing the size count by 1
    
    def pop(self):

        # checking whether the array is empty if empty printing messages and returning none
        if self.size == 0:  
            print("Empty array")
            return None
        
        self.size -= 1 # decreasing the size count by 1
        popped = self.array[self.size]  # saving which element left
        self.array[self.size] = None  # Optional: clear slot
        print(f"Popped: {popped}")  # printing message and returning popped
        return popped

# Lab Demo - testing the code by running all the functions created
print("Dynamic Array Demo")
da = DynamicArray() # object creation

# Append sequence (triggers resize)
print("\n--- APPEND OPERATIONS ---")
da.append(10); da.print_state()
da.append(20); da.print_state()
da.append(30); da.print_state()
da.append(40); da.print_state()  # Triggers resize 4→8
da.append(50); da.print_state()

print("\n--- POP OPERATIONS ---")
da.pop(); da.print_state()
da.pop(); da.print_state()

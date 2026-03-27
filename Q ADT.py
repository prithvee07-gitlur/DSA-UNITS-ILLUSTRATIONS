# ---------------- QUEUE PROGRAM IN PYTHON ----------------
# Queue follows FIFO rule
# FIFO means: First In First Out


# Creating an empty list named queue
# A list is used to store queue elements
queue = []


# ---------------- INSERT OPERATION ----------------
# This function is used to insert an element into the queue
def insert():
    # input() is used to take value from the user
    # int() converts the input into integer
    item = int(input("Enter element to insert: "))
    
    # append() adds the element at the end of the list
    # In queue, insertion always happens at the rear end
    queue.append(item)
    
    # print() displays message on the screen
    print(item, "inserted into queue")


# ---------------- DELETE OPERATION ----------------
# This function is used to delete an element from the queue
def delete():
    # len(queue) checks the number of elements in the queue
    # If queue is empty, deletion is not possible
    if len(queue) == 0:
        print("Queue is empty, cannot delete")
    else:
        # pop(0) removes the first element from the list
        # In queue, deletion always happens from the front
        removed_item = queue.pop(0)
        
        # Display the deleted element
        print(removed_item, "deleted from queue")


# ---------------- TRAVERSAL OPERATION ----------------
# This function is used to display all elements of the queue
def traversal():
    # Check if queue is empty
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue elements are:")
        
        # for loop is used to go through each element in queue
        for element in queue:
            # Print each element one by one
            print(element)


# ---------------- MAIN PROGRAM ----------------
# Infinite loop so that program runs continuously
while True:
    # Display menu options
    print("\nQueue Operations")
    print("1. Insert")
    print("2. Delete")
    print("3. Traversal")
    print("4. Exit")
    
    # Take user choice
    choice = int(input("Enter your choice: "))
    
    # If user chooses 1, call insert function
    if choice == 1:
        insert()
    
    # If user chooses 2, call delete function
    elif choice == 2:
        delete()
    
    # If user chooses 3, call traversal function
    elif choice == 3:
        traversal()
    
    # If user chooses 4, exit the program
    elif choice == 4:
        print("Exiting program")
        break
    
    # If user enters wrong option
    else:
        print("Invalid choice, please try again")
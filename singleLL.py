
# SINGLY LINKED LIST (CORE OPERATIONS)

# IMPLEMENTING DYNAMIC INSERTION AND DELETION WITHOUT SHIFTING

# SINGLY LINKED LIST : Linear data structure of nodes where each node contains data 
#                      + next pointer to the next node. One-way traversal from head to tail (last node's next = null).
 
# ANSWER : 

class Node:
    def __init__(self, data):
        # each node contains data and points to the next node
        self.data = data 
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        # pointing the first node initially none
        self.head = None
    
    def traverse(self):
        # if head is empty then print message and stop
        if not self.head:
            print("List: Empty")
            return
        
        temp = self.head  # storing head in the temp
        result = []  # empty array for storing the results
        while temp:  # while the temp exists
            result.append(str(temp.data)) # adding the data in the result
            temp = temp.next # updating the temp to temp.next
        print("List: " + " → ".join(result))  # printing the result
    
    def insert_begin(self, data):
        new_node = Node(data)   # creating new node
        new_node.next = self.head  # setting the next of new node to head
        self.head = new_node  # and head points to new node
        print(f"Inserted {data} at beginning")  # printing the data
    
    def insert_end(self, data):
        new_node = Node(data)  # creating new node
        if not self.head:  
            # when the self.head is empty , head becomes new node and print the results
            self.head = new_node
            print(f"Inserted {data} at end")
            return
        
        temp = self.head  
        while temp.next: # looping till the end of the list
            temp = temp.next # updating temp to temp.next
        temp.next = new_node   # and temp.next to new node
        print(f"Inserted {data} at end")  # printing the results
    
    def delete_by_value(self, key):
        if not self.head:  # if the list is empty print message and return False
            print("Empty list")
            return False
        
        # Case 1: Delete head
        if self.head.data == key:  # if the head is equal to key then we will be deleted
            self.head = self.head.next
            print(f"Deleted head: {key}")
            return True
        
        # Case 2: Delete middle/tail
        # deleting the element from the tail or middle - searching it and matching the result and
        # deleting the element and then printing the result and then returning True if deleted
        temp = self.head
        while temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                print(f"Deleted: {key}")
                return True
            temp = temp.next  # updating the temp
        
        print(f"{key} not found")  # if not found print message and return False
        return False

# Lab Demo - All operations + edge cases
# code testing by running all the functions
sll = SinglyLinkedList()  # object creation

print("=== Singly Linked List Demo ===\n")

# 1. Insert at beginning
print("1. Insert begin:")
sll.insert_begin(30)
sll.insert_begin(20)
sll.insert_begin(10)
sll.traverse()

# 2. Insert at end
print("\n2. Insert end:")
sll.insert_end(40)
sll.insert_end(50)
sll.traverse()

# 3. Delete cases
print("\n3. Delete HEAD (10):")
sll.delete_by_value(10)
sll.traverse()

print("\n4. Delete MIDDLE (30):")
sll.delete_by_value(30)
sll.traverse()

print("\n5. Delete TAIL (50):")
sll.delete_by_value(50)
sll.traverse()

print("\n6. Delete NON-EXISTENT (99):")
sll.delete_by_value(99)
sll.traverse()


# DOUBLY LINKED LIST (EXTENDED OPERATIONS)

# LEARNING BIDIRECTIONAL LINKS AND CORRECT POINTER UPDATES

# DOUBLY LINKED LIST : A doubly linked list is a type of linked list where each 
#                      node contains a reference to both the next and the previous node. This 
#                      allows for efficient traversal in both directions.

# ANSWER : 

class Node:  # creating a class Node (blueprint)
    def __init__(self, data):  # constructor function - like we have created a new box
        self.data = data  # putting the value in the box created
        self.next = None  # pointing to the next box - initially no next box therefore , None
        self.prev = None  # points to the previous box - initially no next box therefore, None

class DoublyLinkedList:  # creating a class - that is the blueprint for the entire list
    def __init__(self):  # creating an empty list
        self.head = None # head - first in the lst - initially empty (None)
    
    def print_list(self): 

        # if the list is empty, print message and stop
        if not self.head:   
            print("Empty list")
            return
        
        # temp - starting from at the first node
        temp = self.head

        # empty lists to store the values for printing
        forward = []  
        backward = []
        
        # Forward traversal
        while temp:  # while the temp exists keep looping 
            forward.append(str(temp.data)) # writing the current number of the Node
            temp = temp.next # moving to the next node
        
        # Backward traversal 
        temp = self.get_last()  # temp starts from the last person
        while temp:  # while temp exists keep looping in backward direction
            backward.append(str(temp.data))   # writing the number of the Node
            temp = temp.prev   # Move to previous Node (left hand)
        
        print("Forward:  " + " <-> ".join(forward))  # joining the forward elements with <->
        # reversing backward and joining with <-> to match the forward for verification
        print("Backward: " + " <-> ".join(backward[::-1]))  # Reverse to match forward order for verification
        print()
    
    def get_last(self):  # finds the last node
        temp = self.head  # starts at first position
        while temp and temp.next: # while the Node and the next Node exists
            temp = temp.next # keep moving forward
        return temp  # return the last node (who has no next)
    
    def find_target(self, target):   # finding the specific node
        """Find node with target value""" 
        temp = self.head # starting at head and walking forward
        while temp:
            if temp.data == target:  # check whether the data is same as the target node
                return temp  # returning the temp is the match found
            temp = temp.next  # updating temp to the next node
        return None # return none if no match found
    
    def insert_after(self, target, x):  
        """Insert x after node containing target"""
        target_node = self.find_target(target) # finding the node with the target value
        if not target_node:  # if the target not found print error and return False
            print(f"Target {target} not found")
            return False
        
        new_node = Node(x)  # creating a new Node with the value x
        new_node.next = target_node.next  # new node's next points where the target was pointing
        new_node.prev = target_node # new node's prev points to the target
        
        # of the target had something after then update that node's prev to new node
        if target_node.next:  
            target_node.next.prev = new_node
        target_node.next = new_node  # target's next points to the new node ( 10 → 20 becomes 10 ↔ NEW ↔ 20)
        
        return True  # returning True
    
    def delete_at_position(self, pos):
        """Delete node by position"""
        if not self.head:   # handling the empty list and printing message and False
            print("Empty list")
            return False
        
        # Find node at position
        temp = self.head 
        for i in range(pos): # looping till pos steps from the head
            if not temp:  # if node not found at a particular position - error message and False printed
                print("Position out of range")
                return False
            temp = temp.next # updating the temp
        
        if not temp:  # if temp not found at the particular position then print message and return False
            print("Position out of range")
            return False
        
        # Update pointers (handling head/tail)

        # if previous exists then previous skips over deleted Node
        if temp.prev:
            temp.prev.next = temp.next

        # if it is the first node then update head
        else:
            self.head = temp.next  
        
        # if next exists then next node's prev skips over deleted
        if temp.next:
            temp.next.prev = temp.prev
            # No need to update tail explicitly (no tail pointer)
        
        print(f"Deleted: {temp.data}")  # printing what was deleted
        return True  # returning True

# Lab Demo - code execution 
dll = DoublyLinkedList()  # object creation and running all the function to test the code working.

print("=== Doubly Linked List Demo ===\n")

# Build initial list
dll.head = Node(10)
dll.head.next = Node(20)
dll.head.next.prev = dll.head
dll.head.next.next = Node(30)
dll.head.next.next.prev = dll.head.next

print("Initial list:")
dll.print_list()

# Test insert_after
print("1. Insert 15 after 10:")
dll.insert_after(10, 15)
dll.print_list()

print("2. Insert 25 after 20:")
dll.insert_after(20, 25)
dll.print_list()

# Test delete_at_position
print("3. Delete position 1 (15):")
dll.delete_at_position(1)
dll.print_list()

print("4. Delete position 0 (head 10):")
dll.delete_at_position(0)
dll.print_list()

print("5. Delete position 2 (last node):")
dll.delete_at_position(2)
dll.print_list()

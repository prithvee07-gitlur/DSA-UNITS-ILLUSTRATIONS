
# QUEUE USING SLL (O(1) OPERATIONS)

# IMPLEMENTING QUEUE WITH HEAD + TAIL POINTERS AND CONNECT TO BFS USAGE.

# QUEUE USING SLL :  Queue implemented on SLL with front (dequeue) and rear (enqueue) pointers. 
#                    FIFO order. Enqueue at tail O(1), dequeue at head O(1)

# ANSWER :

class Node:
    def __init__(self, data):  
        # each node holds data and points to the next
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # Dequeue from front - first person who leaved first
        self.rear = None   # Enqueue at rear (TAIL POINTER) - last person new people join here
        self.size = 0      # initially empty line
    
    def enqueue(self, data):
        new_node = Node(data) # object creation
        
        # Underflow safe
        if self.rear is None: # empty queue check
            # if the queue is empty them new person becomes both front and rear
            self.front = self.rear = new_node
        else:
            # if the queue is not empty them the rear points to the new person 
            # and updating the rear to new person
            self.rear.next = new_node  # O(1) with tail pointer!
            self.rear = new_node
        
        self.size += 1  # increasing size by 1
        print(f"Enqueued: {data}")  # printing details
    
    def dequeue(self):
        # checking whether the queue is empty or not and printing the messages
        if self.front is None:  
            print("UNDERFLOW: Empty queue")
            return None
        
        # saving that who left from the front and moving the front to the next person
        removed = self.front.data
        self.front = self.front.next
        
        # if front is none then setting the rear to none
        if self.front is None:
            self.rear = None  # Last element removed
        
        self.size -= 1  # size decreased  by 1
        print(f"Dequeued: {removed}")  # printing the details
        return removed  # returning the removed element
    
    def front_element(self):
        if self.front is None:  # if front is none return none
            return None
        else:  # else return the front element 
            return self.front.data
    
    def print_queue(self):
        if not self.front:  # if queue is empty return the message
            print("Queue: Empty")
            return
        
        temp = self.front  # creating a temp variable
        result = []  # empty array for store data
        while temp:  # while the temp exists
            result.append(str(temp.data))  # add the elements to the results 
            temp = temp.next # moving to the next person
        print(f"Queue: {' → '.join(result)} (size={self.size})")  # printing the details


# Lab Demo - code testing by running all the functions 
print("=== Queue using SLL (O(1) operations) ===\n")

q = Queue() # object creation

# Test sequence
print("1. Enqueue operations:")
q.enqueue(10); q.print_queue()
q.enqueue(20); q.print_queue()
q.enqueue(30); q.print_queue()

print("\n2. Dequeue + Front:")
print(f"Front: {q.front_element()}")
q.dequeue(); q.print_queue()

print("\n3. Underflow test:")
q.dequeue(); q.dequeue(); q.dequeue()  # Empty now
q.dequeue()  # UNDERFLOW

print("\n4. BFS-like usage:")
q.enqueue('A'); q.enqueue('B'); q.enqueue('C')
q.print_queue()

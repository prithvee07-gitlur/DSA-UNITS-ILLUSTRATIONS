
# STACK USING SLL + PARENTHESES CHECKER

# BUILDING STACK USING LINKED LIST AND APPLY TO BRACKET VALIDATIONS.

# STACK USING SLL : Stack implemented on top of SLL where top pointer = stack top. 
#                   Push/pop at head (O(1)). LIFO order using SLL nodes.

# ANSWER :

class Node:
    def __init__(self, data):
        # each node contains data and points to the next node
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # setting the top most element none 
        # as initially there is nothing in the stack
    
    def push(self, data):
        new_node = Node(data) # new node created
        new_node.next = self.top  # new node points to the old top 
        # (new plate next-> current top plate)
        self.top = new_node  # top is pointing to the new plate added
    
    def pop(self):
        # checking whether the stack is empty or not 
        # if empty return none
        if not self.top:
            return None
        
        # otherwise pop the element from the top and save it and set the
        # top to the next plate and return the popped element
        popped = self.top.data
        self.top = self.top.next
        return popped
    
    def peek(self):
        # if the top is none return none otherwise return the top element of the stack
        if self.top is None:
            return None
        return self.top.data
    
    def is_empty(self):
        # retuning whether the stack is empty or not (t/f)
        return self.top is None  

def is_valid_parentheses(s):
    stack = Stack()  # new empty stack object
    pairs = {')': '(', ']': '[', '}': '{'}  # pairs or parenthesis dict
    
    for char in s:  # looping through the each character
        if char in pairs:  # Closing bracket - is the bracket is closing ?
            top = stack.pop()   # take the top opening bracket
            if top != pairs[char]:  # does it matches with the closing one ?
                return False
        else:  # Opening bracket
            stack.push(char)  # push the opening bracket into the stack 
    
    return stack.is_empty()  # return if the stack is empty or not 
    # empty stack means valid parenthesis


# Lab Demo - code testing by running all the functions
print("=== Stack using SLL + Parentheses Checker ===\n")

# Test Stack Operations
stack = Stack()
print("Stack Operations:")
stack.push(10); print("Push 10")
stack.push(20); print("Push 20")
stack.push(30); print("Push 30")
print(f"Peek: {stack.peek()}")
print(f"Pop: {stack.pop()}")
print(f"Peek: {stack.peek()}\n")

# Test Parentheses Checker
test_cases = [
    "()", "(())", "({[]})",  # Valid
    ")(", "(()", "([)]",     # Invalid
    "", "abc", "((()))"      # Edge cases
]

print("Parentheses Validation:")
for s in test_cases:
    result = is_valid_parentheses(s)
    print(f"'{s}' → {result}")

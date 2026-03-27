# n = int(input("Enter the number of terms: "))
# a = 0
# b = 1
# print("Fibonacci Series:")

# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

# print() 

def solution(n: int) -> str:
    if n <= 0:
        return "Invalid"
    
    out = ""
    a, b = 0, 1
    for i in range(n):
        out += str(a) + " "
        a, b = b, a + b
    
    return out.strip()
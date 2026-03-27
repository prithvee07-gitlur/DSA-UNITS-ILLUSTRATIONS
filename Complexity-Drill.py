
# COMPLEXITY DRILL (OPEATION COUNTING)

# DEVELOPING INTUITION FOR TIME/SPACE COMPLEXITY USING SIMPLE LOOP 
# STRUCTURES AND CASE ANALYSIS .

# 1. SINGLE LOOP - O(n)

def single_loop(n):   # function defination

    count=0

    for i in range(n):  
         # running single for loop and counting the number of iterations of the 
         # loop for checking its time complexity .
        count+=1

    print("Number of operations performed :",count)  # printing the number of iterations (operations)
    print("Time Complexity - O(n)") # time complexity of single loop
    print(f"Justification : Loop runs {n} times exactly .")  # justification of the time complexity
    print("Linear growth with input size.")



# 2. NESTED LOOP - O(n^2)

def nested_loop(n):  # function defination

    count=0

# running two loops i.e. nested for loop and counting the number of iterations for time complexity
    for i in range(n):
        for j in range(n):
            count+=1

    print(f"Number of operations performed : {count}")  # printing the number of iterations (operations)
    print("Time Complexity - O(n^2)")  # time complexity of nested loop
    print(f"Justification : Outer loop runs {n} times, inner loop runs {n} times each.")  # justification of time complexity
    print("Quadratic Growth - disastrous for large n.")



# 3. TRIANGULAR LOOP - O(n^2)

def triangular_loop(n):  # function defination

    count=0

# running a triangular loop (i.e. loops in which the inner loop runs different number of times as compared to outter loop)
# for counting the number of iteration to calculate the time complexity
    for i in range(1,n+1):  
        for j in range(i):
            count+=1

    print(f"Number of operations performed : {count}")  # printing the number of iterations (operations)
    print("Time Complexity - O(n^2)")  # time complexity of triangular loop
    print(f"Justification : Inner loop is sum to ({n}**2)/2 , n^2/2 operations.")  # justifiaciton of the time complexity
    print("Quardratic Growth - despite it is triangular pattern.")



# 4. HALVING LOOP - O(log(n))

def halving_loop(n):  # defining the function

    count=0
    size=n  

    while size>0:  # running while loop 
        count+=1
        size//=2   # halfing the size of the loop

    print(f"Number of operations performed : {count}")  # printing the number of iterations (operations)
    print("Time Complexity : O(log(n))")  # time complexity of halving loops
    print("Justification : loop runs log base 2 n times.")  # justification of the time complexity
    print("Size halves each iteration.")



def linear_search_cases():   # PRINT LINEAR SEARCH CASES
 
    print("\n Linear Search Case Analysis.")
    print("Best Case : O(1)")
    print("Example : Element at first position.")
    print("Average Case : O(n)")
    print("Example : Element in middle of the list.")
    print("Worst Case : O(n)")
    print("Example : Element at end or absent.")


def binary_search_cases():  # PRINT BINARY SEARCH CASES

    print("\n Binary Search Case Analysis (SORTED DATA REQUIRED !)")
    print("Best Case : O(1)")
    print("Example : Element at middle position.")
    print("Average Case : O(log(n))")
    print("Example : After few divisions.")
    print("Worst Case : O(log(n))")
    print("Example : After maximum division.")


# MAIN DRIVER CODE
def main():
    n=int(input("Enter value of n :"))  
    # taking the number of iterations as an input from the user

    print("\n===Complexity Demo===")

    # CALLING ALL THE FUNCTIONS IN THE MAIN FUNCTION
    single_loop(n)  
    nested_loop(n)
    triangular_loop(n)
    halving_loop(n)

    linear_search_cases()
    binary_search_cases()


if __name__=="__main__":
    main()  # calling the main function


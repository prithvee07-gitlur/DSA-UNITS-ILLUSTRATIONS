def hanoi(n, source, spare, target):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return
    # move n-1 disks from source to spare
    hanoi(n - 1, source, target, spare)

    # move the biggest disk from source to target
    print("Move disk", n, "from", source, "to", target)

    # move n-1 disks from spare to target
    hanoi(n - 1, spare, source, target)

# Time Complexity: O(2^n) - total moves = 2^n - 1
# Space Complexity: O(n) - because of recursive function calls
n = int(input("Enter number of disks: "))

print("Steps to solve Tower of Hanoi with", n, "disks:")
hanoi(n, "A", "B", "C")

"""what is single link list and discuss about time complexity of all operations"""
""" time space tradeoff """
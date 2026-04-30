def bubbleSort(nums: list[int]):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1] , nums[j]

def main():
    lis = [3,-1,2,4,0]
    bubbleSort(lis)
    print(lis)

main()

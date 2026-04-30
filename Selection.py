def selectionSort(nums: list[int]):
    n = len(nums)
    for i in range(n-1):
        minInd = i
        for j in range(i+1, n):
            if nums[j] < nums[minInd]:
                minInd = j
        nums[i] , nums[minInd] = nums[minInd] , nums[i]

def main():
    lis = [3,-1,2,4,0]
    selectionSort(lis)
    print(lis)

main()

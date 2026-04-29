# INSERTION SORT

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
        arr[j+1]=key
    return arr

print(insertion_sort([23,24,12,5,14,74]))

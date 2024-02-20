# Binary search is efficient for sorted data structures and divides the search space in half.

def binary_search(arr, target):
    low, high=0,len(arr)-1
    mid=(high+low)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        low=mid+1
    else:
         high=mid-1
    return -1

data=[11,21,31,44,55,66,77,88]
target=44
result=binary_search(data,target)

if result!=-1:
    print(f"{target} is found at index {result}.")
else:
    print(f"{target} element is not found inside the array.")

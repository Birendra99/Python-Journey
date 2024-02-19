#Linear search is a simple method that checks each element sequentially until a match is found


def linear_Search(arr, target):
    for i, element in enumerate(arr):
        if(element==target):
            return i
    return -1

data=[11,12,13,14,15,16,17,18]
target=16
result=linear_Search(data,target)

if result!=-1:
    print(f"{target} is found at index {result}")
else:
    print(f"{target} is not found in the data")
    
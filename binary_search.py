def iterative_binary_search(arr,left,target,right):
    while(left <= right):
        mid = (right - left)//2 + left
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        if arr[mid] > target:
            right = mid - 1
    return -1

arr = [1,2,3,7,8]
print(iterative_binary_search(arr,0,388,4))


def recursive_binary_search(arr,left,right,target):
    if left <= right:
        mid = (right - left)//2 + left
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return recursive_binary_search(arr,mid+1,right,target)
        else:
            return recursive_binary_search(arr,left,mid-1,target)
    else:
        return -1
    

arr = [1,2,3,7,8]
print(recursive_binary_search(arr,0,4,1233))





def lower_bound(nums,value):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left+right)//2
        if nums[mid] < value:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(nums,value):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left+right)//2
        if nums[mid] <= value:
            left = mid +1
        else:
            right = mid
    return left


arr = [0,1,4,8,9,11,12]
print(lower_bound(arr,15))
print(upper_bound(arr,15))








def lower_bound(arr,value):
    left = 0
    right = len(arr)
    while left <= right:
        mid = (left + right)//2
        if arr[mid] < value:
            left = mid +1
        else:
            right = mid
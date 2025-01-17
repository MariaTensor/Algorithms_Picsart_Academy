def searchRange(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start+end) //2
        if nums[start] == nums[end] == target:
            return [start, end]
        if nums[mid] > target:
            end = mid -1
        elif nums[mid] < target:
            start = mid + 1
        else:
            if nums[start] != target:
                start +=1
            if nums[end] != target:
                end -= 1
    return [-1,-1]

print(searchRange([1,2,3,4,4,4,4,6],4))
        


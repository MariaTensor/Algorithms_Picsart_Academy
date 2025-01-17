arr = [1,7,3,5,6,5]
nums = [1,-1,4]

def pivot_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

# print(pivot_index(arr))
# print(pivot_index(nums))


def pivot_index_2(nums):
    if len(nums) == 0:
        return -1
    leftSum = 0
    rightSum = 0
    for i in nums:
        rightSum += i
     
    for i in range(len(nums)):
        rightSum -= nums[i]
        if(rightSum == leftSum):
            return i
        leftSum += nums[i]

    return -1

# print(pivot_index_2(arr))
print(pivot_index_2(nums))

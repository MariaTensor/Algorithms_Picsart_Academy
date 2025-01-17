def two_sum(nums,target):
    numbers = {}
    for i in nums:
        numbers[i] = target -i
    for key in numbers:
        if numbers[key] in nums:
            if numbers[key] == key and nums.count(numbers[key]) == 1:
                continue
            else:
                return [nums.index(key), nums.index(numbers[key], nums.index(key) + 1, len(nums))]
            return [nums.index(key),nums.index(numbers[key])]

            
    
def two_sum_2(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            

def two_sum3(nums, target):
    numbers = {}
    for i,num in enumerate(nums):
        comp = target - num
        if comp in numbers:
            return [numbers[comp],i]
        numbers[num] = i
    return None            

arr = [3,4,2]
# arr = [3,1,3]
# print(two_sum_2(arr,6))
print(two_sum3(arr,6))

        
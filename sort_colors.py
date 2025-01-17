def sort_colors(nums):
    zero,one,two = 0,0,len(nums) - 1
    while one <= two:
        if nums[one] == 0:
            nums[one],nums[zero] = nums[zero],nums[one]
            one += 1
            zero += 1
        elif nums[one] == 1:
            one += 1
        else:
            nums[one],nums[two] = nums[two],nums[one]
            two -= 1

nums = [2,0,2,1,1,0]
nums2 = [1,0,2]
print(nums)
sort_colors(nums)
sort_colors(nums2)
print(nums) 
print(nums2)

arr = [1,2,3,4,5,6,7]
# k = 3
# for i in range(k):
#     arr[:] = arr[len(arr) - 1:] + arr[:-1]


nums = [-1,-100,3,99]
k = 2
for i in range(len(nums)//k):
    nums[:] = nums[len(nums) - 1:] + nums[:-1]

print(arr)
print(nums)
#[7,1,2,3,4,5,6]
#[6,7,1,2,3,4,5]
#[5,6,7,1,2,3,4]
# arr[0] = arr[6] arr[1] = arr[2]  


def rotate_array(nums,k):
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]


        

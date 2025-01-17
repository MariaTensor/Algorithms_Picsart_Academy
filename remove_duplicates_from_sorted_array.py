def removeDuplicates(arr):
    arr[:] = sorted(set(arr))
    print(len(arr))
    return len(arr)


def removeDuplicates(self, nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j
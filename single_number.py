def singleNumber(self, nums):
    num = 0
    for i in nums:
        num ^= i
    return num 
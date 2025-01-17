
nums = [6,9,10]
nums2 = [3,3]
def gcd(nums):
    a,b = min(nums),max(nums)
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(nums))

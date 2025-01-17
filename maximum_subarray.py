def max_crossing_subarray(arr,low,mid,high):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid,low-1,-1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    for i in range(mid+1,high+1):
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    return left_sum + right_sum

def max_subarray(arr,low,high):
    if high == low:
        return arr[low]
    else:
        mid = (low + high) //2
        left_low,left_high = low,mid
        left_sum = max_subarray(arr,left_low,left_high)
        right_low,right_high = mid+1,high
        right_sum = max_subarray(arr,mid+1,high)
        cross_low,cross_high = low,high
        cross_sum = max_crossing_subarray(arr,low,mid,high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_sum
        else:
            return cross_sum


arr = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [1]
# print(max_subarray(nums,0,len(nums) -1))
# print(max_subarray(nums2,0,len(nums2) - 1))



def max_sub(arr):
    res = []
    for i in range(len(arr)):
        sum = arr[i]
        max_sum = sum
        for j in range(i+1,len(arr)):
                sum += arr[j]
                if sum > max_sum:
                    max_sum = sum
        res.append(max_sum)
    return max(res)

print(max_sub(arr))



def max_sub2(arr):
    max_sum = float('-inf')
    cur_sum = 0
    for i in arr:
        cur_sum += i
        max_sum = max(max_sum,cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return max_sum

print(max_sub2(arr))



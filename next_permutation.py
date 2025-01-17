arr = [1,3,5,6,2]
arr2 = [1,2,3]

def next_permutation(arr):
    n = len(arr)
    pivot = -1
    for i in range(n-1,0,-1):
        if arr[i] > arr[i - 1]:
            pivot = i -1
            break
    if pivot == -1:
        arr.reverse()
        return arr
    diff_idx = -1
    for i in range(n-1,pivot,-1):
        if arr[i] > arr[pivot]:  
            diff_idx = i
            break
    arr[pivot], arr[diff_idx] = arr[diff_idx], arr[pivot]
    arr[pivot + 1:] = arr[pivot + 1:][::-1]
    return arr


# print(next_permutation(arr))
# print(next_permutation(arr2))



def next_permutation(arr):
    pivot = -1
    for i in range(len(arr) - 1, 0,-1):
        if arr[i] > arr[i - 1]:
            pivot = i
            break
    if pivot == -1:
        arr.reverse()
        return arr
    diff_index = -1
    for i in range(len(arr) -1, pivot,-1):
        if arr[i] > arr[pivot]:
            diff_index = i
            break
    arr[pivot],arr[diff_index] = arr[diff_index],arr[pivot]
    arr[pivot+1:] = arr[pivot + 1:][::-1]
    return arr

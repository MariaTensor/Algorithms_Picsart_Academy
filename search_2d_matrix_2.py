matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5



def binary_search(arr,target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def search_2d_2(matrix,target):
    tmp = False
    for i in matrix:
        tmp = binary_search(i,target)
        if tmp:
            return tmp
    return tmp
    

print(search_2d_2(matrix,target))
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

def search(matrix,target):
    tmp = []
    for i in matrix:
        tmp.extend(i)
    for i in tmp:
        if target ^i == 0:
            return True
    return False

def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    print(right)
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // n][mid % n]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

print(searchMatrix(matrix,target))
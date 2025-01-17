def insertion(arr):
    for i in range(1,len(arr)):
        j = i - 1
        tmp = arr[i]
        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            arr[j] = tmp
            j = j - 1
    return arr

arr = [5,2,6,0,8,-1]
print(insertion(arr))

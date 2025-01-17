def partition(arr,low,high):
    i = low
    j = high - 1
    while i <= j:
        if arr[i] <= arr[high]:
            i += 1
        elif arr[j] > arr[high]:
            j -= 1
        else:
            arr[i],arr[j] = arr[j],arr[i]
    arr[i],arr[high] = arr[high],arr[i]
    return i

def partition_last(arr,low,high):
    i = low
    pi = arr[high]
    for j in range(low,high):
        if arr[j] < pi:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
    arr[i],arr[high] = arr[high],arr[i]
    return i
def quick_sort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi + 1,high)


arr = [10,7,8,9,1,5]
quick_sort(arr,0,len(arr) -1)
print(arr)



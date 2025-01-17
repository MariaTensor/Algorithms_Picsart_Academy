def counting_sort(arr,exp):   #Complexity O(d*(k+n)) d-number of digits in the max_val, n- size of arr, k- range of digits
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    for i in range(1,10):
        count[i] += count[i-1]

    for i in range(n-1,-1,-1):
        index = (arr[i]//exp) % 10
        output[count[index]-1] = arr[i]
        count[index] -= 1
    for i in range(n):
        arr[i] = output[i]
    return arr[i]


def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr,exp)
        exp *= 10


















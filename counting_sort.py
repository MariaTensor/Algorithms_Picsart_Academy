def count_sort(input_arr):
    max_val = max(input_arr)
    count_arr = [0] * (max_val + 1)
    for num in input_arr:
        count_arr[num] += 1
    for i in range(1,max_val + 1):
        count_arr[i] = count_arr[i-1] + count_arr[i]
    output_arr = [0] * len(input_arr)
    for i in range(len(input_arr)- 1,-1,-1):
        output_arr[count_arr[input_arr[i]] - 1] = input_arr[i]
        count_arr[input_arr[i]] -= 1
    return output_arr


input_array = [4, -3, 12, 1, 5, 5, 3, 9]

print(count_sort(input_array))
   
def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    min_val = min(arr)
    max_val = max(arr)
    n = len(arr)
    bucket_range = (max_val-min_val)/n
    buckets = [[] for _ in range(n)]
    for num in arr:
        index = int((num-min_val) / bucket_range)
        if index == n:
            index -= 1
        buckets[index].append(num)
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))
    return sorted_array



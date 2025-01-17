arr = [4,2,5,7]

def sort(arr):
    dir = {"even":[],"odd":[]}
    for i in arr:
        if i %2 == 0:
            dir["even"].append(i)
        else:
            dir['odd'].append(i)
    for i in range(len(arr)):
        if i % 2 == 0:
            arr[i] = dir['even'][0]
            dir["even"] = dir['even'][1:]
        else:
            arr[i] = dir["odd"][0]
            dir["odd"] = dir['odd'][1:]
    return arr

print(sort(arr))
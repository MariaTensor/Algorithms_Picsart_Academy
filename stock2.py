prices = [7,1,5,3,6,4]
prices2 = [1,2,3,4,5]
prices3 = [7,6,4,3,1]

def stock_two(arr):
    res = []
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] > 0:
            res.append((arr[i+1] - arr[i]))
    return sum(res)

print(stock_two(prices))
print(stock_two(prices2))
print(stock_two(prices3))

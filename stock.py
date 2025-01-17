def foo(arr):
    minimum = arr[0]
    max_profit = 0
    for i in arr:
        minimum = min(i,minimum)
        max_profit = max(i-minimum,max_profit)
    return max_profit

prices = [7,1,5,3,6,4]
print(foo(prices))
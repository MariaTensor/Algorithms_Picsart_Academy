def transform(s):
    res,prev = 0,0
    romanValues = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    for i in s[::-1]:
        if romanValues[i] >= prev:
            res += romanValues[i]
        else:
            res -= romanValues[i]
        prev = romanValues[i]
    return res


        

def number_of_jewels(jewels,stones):
    count = 0
    for i in set(stones):
        if i in jewels:
            count += 1
    return count


print(number_of_jewels("z","ZZ"))

def number_of_jewels(jewels,stones):
    count = [0] * 128
    for stone in stones:
        count[ord(stone)] += 1
    res = 0
    for jewel in jewels:
        res += count[ord(jewel)]
    return res
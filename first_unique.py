def firstUniqChar(s: str) -> int:
    arr = [0] * 128
    for i in s:
        arr[ord(i)] += 1
    print(arr)
    for index, char in enumerate(s):
        if arr[ord(char)] == 1:
            return index

    return -1


def firstUnique(s):
    seenonce = 0
    seentwice = 0
    for char in s:
        bit_pos = 1<<(ord(char) - ord('a'))

        if seenonce & bit_pos:
            seenonce &= ~bit_pos
            seentwice |= bit_pos
        else:
            if not(seentwice & bit_pos):
                seenonce |= bit_pos
    for i, char in enumerate(s):
        bit_pos = 1 << (ord(char) - ord('a'))
        if seenonce & bit_pos:
            return i
    return -1

s = 'leetcode'

print(firstUnique(s))
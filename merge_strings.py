def merge_strings(word1,word2):
    res = ""
    min_len = min(len(word1),len(word2))
    i = 0
    for i in range(min_len):
        res += word1[i]
        res += word2[i]
        i += 1
    if word1[i:]:
        res += word1[i:]
    if word2[i:]:
        res += word2[i:]
    
    return res

word1 = "abc"
word2 = "pqr"

word3 = "ab"
word4 = "pqrs"

word5 = "abcd"
word6 = "pq"

print(merge_strings(word1,word2))
print(merge_strings(word3,word4))
print(merge_strings(word5,word6))
# print(word1[2:])


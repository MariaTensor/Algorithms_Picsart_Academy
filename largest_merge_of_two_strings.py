word1 = "cabaa"
word2 = "bcaaa"


def merge_strings(word1,word2):
    res = ""
    i,j = 0,0
    while i < len(word1) and j < len(word2):
        if word1[i] > word2[j]:
            res += word1[i]
            i+=1
        elif word1[i] > word2[j]:
            res += word2[j]
            j += 1
        else:
            if word1[i:] > word2[j:]:
                res+= word1[i]
                i+=1
            else:
                res+= word2[j]
                j+=1
    return res + word1[i:]+word2[j:] 



word3 = "abcabc"
word4 = "abdcaba" 
print(merge_strings(word1,word2))
print(merge_strings(word3,word4))

def is_palindrome(num):
    tmp = num
    rev = 0
    if tmp > 0:
        while tmp != 0:
            rev = 10* rev + tmp % 10
            tmp = tmp //10
    return rev == num

print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(1997))
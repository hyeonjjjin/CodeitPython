def is_palindrome(word):
    for i in range(int(len(word)/2)):
        if word[i] != word[len(word)-i-1]:
            return False
    return True


print(is_palindrome("hello"))
print(int(36 / 3))

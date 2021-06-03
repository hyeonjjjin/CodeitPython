def is_palindrome(word):
    temp1 = word[0:(len(word) / 2)]
    temp2 = word[len(word) / 2 + 1 + (len(word) % 2):]
    print(temp1)
    print(temp2)
    for i in range(len(temp1)):
        print()


print(is_palindrome("racecar"))
print(int(36 / 3))

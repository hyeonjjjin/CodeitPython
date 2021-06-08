def is_palindrome(word):
    for i in range(int(len(word) / 2)):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


def linear_search(element, some_list):
    for i in range(len(some_list)):
        if element == some_list[i]: return i
    return None
    # 코드를 작성하세요.


def binary_search(element, some_list):
    mid = int(len(some_list) / 2) - 1 + (len(some_list) % 2)
    while 1:
        if some_list[mid] == element:
            return mid
        elif some_list[mid] > element:
            mid = int(mid / 2)
        else:
            mid += int(mid/2) + 1 - mid % 2
        if mid == 0 and some_list[mid] != element:
            return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

print(linear_search(11, [2, 3, 5, 7, 11]))

print(is_palindrome("hello"))

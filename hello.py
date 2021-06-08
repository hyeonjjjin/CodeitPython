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
            mid += int(mid / 2) + 1 - mid % 2
        if mid == 0 and some_list[mid] != element:
            return None


def selection_sort(some_list):
    for i in range(len(some_list)-1):
        if min(some_list[i+1:]) < some_list[i]:
            index = some_list.index(min(some_list[i+1:]))
            tmp = some_list[i]
            some_list[i] = some_list[index]
            some_list[index] = tmp

    return some_list


def bubble_sort(some_list):
    for i in range(len(some_list)):
        min = some_list[i]
        swap = i
        for j in range(i+1, len(some_list)):
            if some_list[j] < min:
                min = some_list[j]
                swap = j
        if swap != i:
            tmp = some_list[i]
            some_list[i] = some_list[swap]
            some_list[swap] = tmp

    return some_list


print(bubble_sort([6, 2, 7, 3, 1, 2]))

print(selection_sort([6, 2, 7, 3, 1, 2]))

print(binary_search(11, [2, 3, 5, 7, 11]))

print(linear_search(11, [2, 3, 5, 7, 11]))

print(is_palindrome("hello"))

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


# 이진 탐색 1
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


# 이진 탐색 2
def binary_search2(element, some_list):
    start = 0
    end = len(some_list) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if some_list[mid] == element:
            return mid
        elif some_list[mid] > element:
            end = mid - 1
        else:
            start = mid + 1
    return None


def selection_sort(some_list):
    for i in range(len(some_list) - 1):
        if min(some_list[i + 1:]) < some_list[i]:
            index = some_list[i + 1:].index(min(some_list[i + 1:])) + i + 1
            tmp = some_list[i]
            some_list[i] = some_list[index]
            some_list[index] = tmp
    return some_list


def selection_sort2(some_list):
    for i in range(len(some_list)):
        minimum = some_list[i]
        swap = i
        for j in range(i + 1, len(some_list)):
            if some_list[j] < minimum:
                minimum = some_list[j]
                swap = j
        if swap != i:
            tmp = some_list[i]
            some_list[i] = some_list[swap]
            some_list[swap] = tmp

    return some_list


# Recursive 재귀
def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


# O(2^n)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def triangle_number(n):
    if n == 1:
        return 1
    else:
        return n + triangle_number(n-1)


def sum_digits(n):
    if len(str(n)) == 1:
        return n
    else:
        return int(n / (10 ** (len(str(n)) - 1))) + sum_digits(n % (10 ** (len(str(n)) - 1)))


def flip(some_list):
    if len(some_list) > 1:
        return [some_list[len(some_list)-1]]+flip(some_list[:len(some_list)-1])
    else:
        return [some_list[0]]


print(flip([1, 2, 3, 4, 5]))

print(sum_digits(5342))

print(triangle_number(3))

print(fib(7))

print(factorial(5))

countdown(4)

print(selection_sort([6, 2, 7, 3, 1, 2]))

print(selection_sort2([6, 2, 7, 3, 1, 2]))

print(binary_search2(11, [2, 3, 5, 7, 11]))

print(linear_search(11, [2, 3, 5, 7, 11]))

print(is_palindrome("hello"))

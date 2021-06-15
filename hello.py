def is_palindrome(word):
    for i in range(int(len(word) / 2)):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


def linear_search(element, some_list):
    for i in range(len(some_list)):
        if element == some_list[i]:
            return i
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
        return n + triangle_number(n - 1)


def sum_digits(n):
    if len(str(n)) == 1:
        return n
    else:
        return int(n / (10 ** (len(str(n)) - 1))) + sum_digits(n % (10 ** (len(str(n)) - 1)))


def flip(some_list):
    if len(some_list) > 1:
        return some_list[-1:] + flip(some_list[:-1])
    else:
        return [some_list[0]]


def binary_search_recursion(element, some_list, start_index=0, end_index=None):
    if end_index is None:
        end_index = len(some_list) - 1
    if start_index > end_index:
        return None
    mid_index = (start_index + end_index) // 2
    if element == some_list[mid_index]:
        return mid_index
    else:
        if element > some_list[mid_index]:  # list 그대로 주고 start, end index 지정해주는 방법도 있다
            return mid_index + 1 + binary_search_recursion(element, some_list[mid_index + 1:])
        else:
            return binary_search_recursion(element, some_list[:mid_index])


# hanoi 2^n
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    oth_peg = 6 - (start_peg + end_peg)
    if num_disks == 0:
        return
    else:
        hanoi(num_disks - 1, start_peg, oth_peg)
        move_disk(num_disks, start_peg, end_peg)
        hanoi(num_disks - 1, oth_peg, end_peg)


# Brute Force Attack
def max_product(left_cards, right_cards):
    all_mul = []
    for left in range(len(left_cards)):
        for right in range(len(right_cards)):
            all_mul.append(left_cards[left]*right_cards[right])
    return max(all_mul)


def max_product_feedback(left_cards, right_cards):
    product = left_cards[0] * right_cards[0]
    for left in left_cards:
        for right in right_cards:
            product = max(max_product, left * right)
    return product


print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))

hanoi(3, 1, 3)
print(binary_search_recursion(3, [2, 3, 5, 7, 11]))
print(binary_search_recursion(11, [2, 3, 5, 7, 11]))

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

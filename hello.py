# 알고리즘 패러다임

from math import sqrt


def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


def closest_pair(coordinates):
    answer = [coordinates[0], coordinates[1]]
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            if distance(answer[0], answer[1]) >= distance(coordinates[i], coordinates[j]):
                answer = [coordinates[i], coordinates[j]]
    return answer


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
            all_mul.append(left_cards[left] * right_cards[right])
    return max(all_mul)


def max_product_feedback(left_cards, right_cards):
    product = left_cards[0] * right_cards[0]
    for left in left_cards:
        for right in right_cards:
            product = max(max_product, left * right)
    return product


def trapping_rain(buildings):
    answer = 0
    maxHigh = max(buildings)
    leftMax = {}
    rightMax = {}
    for i in range(1, len(buildings) - 1):
        leftMax[i] = max(buildings[:i])
        rightMax[i] = max(buildings[i + 1:])
    for x in range(1, len(buildings) - 1):
        for y in range(buildings[x], maxHigh + 1):
            if leftMax[x] > y and rightMax[x] > y:
                answer += 1
    return answer


def trapping_rain_feedback(buildings):
    total_height = 0
    for i in range(1, len(buildings) - 1):
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])
        # 현재 인덱스에 담길 수 있는 최대 높이
        upper_bound = min(max_left, max_right)

        # 현재 건물 높이가 더 높다면 물이 담길 수 없음
        # 건물 높이가 담길 수 있는 최대 높이보다 높을 수 있기 때문에 max 함수 사용. 담길 수 있다해도 내 높이 빼야함
        total_height += max(0, upper_bound - buildings[i])

    return total_height


def consecutive_sum(start, end):
    if end == start:
        return start
    return consecutive_sum(start, (start+end)//2)+consecutive_sum((start+end)//2+1, end)


# 정렬된 두 리스트를 받아 하나의 정렬된 리스트로 리턴
def merge(list1, list2):
    answer = []
    while len(list1) > 0 or len(list2) > 0:
        if len(list1) == 0:
            answer.append(list2[0])
            del list2[0]
        elif len(list2) == 0:
            answer.append(list1[0])
            del list1[0]
        elif list1[0] < list2[0]:
            answer.append(list1[0])
            del list1[0]
        else:
            answer.append(list2[0])
            del list2[0]
    return answer


# 두 리스트 중 하나만 비어도 반복문을 나오게 하고 나머지를 한번에 넣어줌
def merge_feedback(list1, list2):
    i = 0
    j = 0
    merged_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    merged_list = merged_list + list1[i:] + list2[j:]

    return merged_list


def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list
    else:
        return merge(merge_sort(my_list[:len(my_list)//2]), merge_sort(my_list[len(my_list)//2:]))
    # 받은 리스트를 쪼개야 정렬할 수 있어
    # 근데 쪼개진 리스트도 정렬되어있지 않으니 쪼개야 정렬할 수 있어
    # 최종적으로 길이가 0-1인 리스트로 쪼개야 merge 함수를 통해 정렬된 리스트로 합칠 수 있어
    # 길이가 0-1인 리스트로 쪼개진 경우 merge 함수에 보내서 합쳐
    # 합쳐진 리스트는 정렬된 상태일 테니 그대로 다시 merge 함수에 대입될 수 있어
    # 상호반복.. 을 통해 정렬 되는거다!


# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    swap = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = swap
    # my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    b = i = start
    while i < end:
        if my_list[i] <= my_list[end]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1
    swap_elements(my_list, b, end)
    end = b
    return end


def quicksort(my_list, start, end):
    if end-start < 0:
        return
    else:
        newpivot = partition(my_list, start, end)
        quicksort(my_list, start, newpivot-1)
        quicksort(my_list, newpivot+1, end)


# 옵셔널 파라미터(Optional Parameter) 사용!
def quicksort2(my_list, start=0, end=None):
    if end is None:
        end = len(my_list)-1
    if end - start < 0:
        return
    else:
        newpivot = partition(my_list, start, end)
        quicksort(my_list, start, newpivot - 1)
        quicksort(my_list, newpivot + 1, end)


def fib_memo(n, cache):
    if n < 3:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
        return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}
    return fib_memo(n, fib_cache)


def fib_tab(n):
    fib_table = [0, 1, 1]
    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])
    return fib_table[n]


def fib_optimized(n):
    current = 1
    previous = 0
    for i in range(2, n + 1):
        current, previous = current+previous, current
    return current


def max_profit_memo(price_list, count, cache):
    if count == 1:
        return price_list[count]
    elif count in cache:
        return cache[count]
    else:
        a, b, maxProfit = 1, count-1, 0
        if b+1 <= len(price_list)-1:
            maxProfit = price_list[b+1]
        while a <= b:
            temp = max_profit_memo(price_list, a, cache) + max_profit_memo(price_list, b, cache)
            if temp > maxProfit:
                maxProfit = temp
            a += 1
            b -= 1
        cache[count] = maxProfit
        return cache[count]


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))

print(fib_optimized(16))
print(fib_tab(10))
print(fib(10))

list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort2(list2) # start, end 파라미터 없이 호출
print(list2)
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge([1], []))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))

print(consecutive_sum(1, 10))

print("trapping rain")
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))

print(max_product([1, 6, 5], [4, 2, 3]))

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

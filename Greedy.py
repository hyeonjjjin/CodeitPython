# Greedy
def min_coin_count(value, coin_list):
    count, i = 0, 0
    coin_list.sort(reverse=True)
    for coin in sorted(coin_list, reverse=True):
        count += (value // coin)
        value %= coin

    return count


def max_product(card_lists):
    answer = 1
    for card_list in card_lists:
        answer *= max(card_list)
    return answer


def min_fee(pages_to_print):
    if len(pages_to_print) == 1:
        return pages_to_print[0]
    return sorted(pages_to_print)[0] * len(pages_to_print) + min_fee(sorted(pages_to_print)[1:])
    '''
    sorted_list = sorted(pages_to_print)
    # 총 벌금을 담을 변수
    total_fee = 0

    # 정렬된 리스트에서 총 벌금 계산
    for i in range(len(sorted_list)):
        total_fee += sorted_list[i] * (len(sorted_list) - i)

    return total_fee
    '''


# 가장 먼저 끝나는 강의를 찾는 Greedy를 이용하면 최적의 답을 찾을 수 있다.
def course_selection(course_list):
    answer = {course_list[0]}
    index, end, min = 0, 0, course_list[0][1]
    for i in range(1, len(course_list)):
        if course_list[i][0] > end and course_list[i][1] < min:
            min = course_list[i][1]
            index = i
    end = course_list[index][0]
    answer.append(course_list[index])


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))

# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))


# 테스트
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
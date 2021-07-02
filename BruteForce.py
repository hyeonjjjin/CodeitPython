# Brute Force Attack
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


print("trapping rain")
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))

print(max_product([1, 6, 5], [4, 2, 3]))

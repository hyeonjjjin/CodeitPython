# Greedy
def min_coin_count(value, coin_list):
    count, i = 0, 0
    coin_list.sort(reverse=True)
    while value > 0 and i < len(coin_list):
        if value >= coin_list[i]:
            value -= coin_list[i]
            count += 1
        else:
            i += 1
    return count


# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
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
        if count < len(price_list):
            maxProfit = price_list[count]
        for i in range(1, count//2+1):
            maxProfit = max(maxProfit, max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count-i, cache))
        cache[count] = maxProfit
        return cache[count]


def max_profit_memoization(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


def max_profit_tabulation(price_list, count):
    max_profit_table = [price_list[0], price_list[1]]
    for i in range(2, count + 1):
        maxProfit = 0
        if i < len(price_list):
            maxProfit = price_list[i]
        for j in range(1, i // 2 + 1):
            maxProfit = max(maxProfit, max_profit_table[j] + max_profit_table[i-j])
        max_profit_table.append(maxProfit)
    return max_profit_table[count]


print(max_profit_tabulation([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit_tabulation([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit_tabulation([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))

print(max_profit_memoization([0, 100, 400, 800, 900, 1000], 5))
print(fib_optimized(16))
print(fib_tab(10))
print(fib(10))
# cost = int(input())
# N = int(input())
#
# money_map = [list(map(int, input().split())) for _ in range(N)]
#
# money_dict = dict()
#
# for i in money_map:
#     money_type, amount = i
#     money_dict[money_type] = amount
#
# # 10원을 1, 2, 3, 4, 5, ... 개 썼을 때
# # 그 중에
# # 5 원을 1, 2, 3, 4, 5 ... 개 썼을 때
# # 그 중에
# # 1 원을 1, 2, 3, 4, 5 ... 개 썼을 때
#
#
# count = 0
#
# def recur(money_value: int, rest_money):
#     global count
#
#     if money_value == N or rest_money < 0:
#         return
#
#     for i in range(money_map[money_value][1] + 1):
#         if rest_money - (money_map[money_value][0] * i) == 0:
#             count += 1
#             continue
#         else:
#             recur(money_value + 1, rest_money - (money_map[money_value][0] * i))
#
#
# recur(0, cost)
#
# print(count)


target = int(input())
N = int(input())

coins = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(target + 1)]
dp[0] = 1


def calculate(coin_idx):
    global dp

    tmp = dp.copy()

    coin_value, coin_count = coins[coin_idx]
    for i in range(1, coin_count + 1):
        for available_count in range(len(dp)):
            if available_count + (coin_value * i) > target:
                break

            if dp[available_count] != 0:
                tmp[available_count + (coin_value * i)] += dp[available_count]

    dp = tmp


for i in range(len(coins)):
   calculate(i)


print(dp[-1])

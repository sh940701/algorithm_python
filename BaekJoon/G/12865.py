N, K = list(map(int, input().split()))
objects = [list(map(int, input().split())) for _ in range(N)]



# result_value = float('-inf')
#
#
# def recur(idx, weight, value):
#     global result_value
#
#     if weight > K:
#         return
#     elif idx == N:
#         result_value = max(result_value, value)
#         return
#
#     # 물건을 챙길 때
#     recur(idx + 1, weight + objects[idx][0], value + objects[idx][1])
#     # 물건을 안 챙길 때
#     recur(idx + 1, weight, value)
#
#
# recur(0, 0, 0)
#
# print(result_value)

dp = [[-1] * (K + 1) for _ in range(N)]


def recur(idx, weight):
    if weight > K:
        return float('-inf')
    if idx == N:
        return 0
    if dp[idx][weight] != -1:
        return dp[idx][weight]

    dp[idx][weight] = max(recur(idx + 1, weight + objects[idx][0]) + objects[idx][1], recur(idx + 1, weight))

    return dp[idx][weight]


print(recur(0, 0))

# def recur(cur, w):
#     if w > m:
#         return -9999999
#
#     if cur == n:
#         return 0
#
#     if dp[cur][w] != -1:
#         return dp[cur][w]
#
#     dp[cur][w] = max(recur(cur + 1, w + arr[cur][0]) + arr[cur][1], recur(cur + 1, w))
#
#     return dp[cur][w]
#
#
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for i in range(n)]
#
# dp = [[-1 for _ in range(100010)] for j in range(n)]
#
# ans = recur(0, 0)
#
# print(ans)

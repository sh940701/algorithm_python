N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# result = float('-inf')
#
#
# def recur(idx, benefit):
#     global result
#
#     if idx == N:
#         result = max(result, benefit)
#         return
#     # 퇴사일 이후에는 일을 할 수 없음
#     if idx > N:
#         return
#
#     # 상담을 할 때
#     # 다른 상담을 하고 있는 중에는 상담을 할 수 없음
#     recur(idx + arr[idx][0], benefit + arr[idx][1])
#
#     # 상담을 하지 않을 때
#     recur(idx + 1, benefit)
#
#
# recur(0, 0)
#
# print(result)

# DP memoization 활용

dp = [0] * N


def recur(idx):
    if idx == N:
        return 0

    if idx > N:
        return float('-inf')

    if dp[idx]:
        return dp[idx]

    dp[idx] = max(recur(idx + arr[idx][0]) + arr[idx][1], recur(idx + 1))

    return dp[idx]


recur(0)

print(max(dp))

N = int(input())

houses = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(3)]


def recur(idx, color):
    if idx == N:
        return 0

    if dp[idx][color]:
        print('cost: ', dp[idx][color])
        return dp[idx][color]

    for i in range(3):
        dp[idx][i] = (
            min(
                recur(idx + 1, (i + 1) % 3) + houses[idx][(i + 1) % 3],
                recur(idx + 1, (i + 2) % 3) + houses[idx][(i + 2) % 3]
            ) + houses[idx][i]
        )

    return dp[idx][color]


print(recur(0, -1))

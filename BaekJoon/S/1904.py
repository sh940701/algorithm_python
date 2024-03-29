N = int(input())

dp = [0] * (N + 2)

dp[0] = 0
dp[1] = 1

for i in range(2, N + 2):
    dp[i] = ((dp[i - 1] % 15746) + dp[i - 2] % 15746) % 15746

print(dp[N + 1])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = (0, tuple(arr[i]))

print(*dp, sep='\n')

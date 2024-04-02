N = int(input())
nums = list(map(int, input().split()))

q_N = int(input())

q_arr = [list(map(int, input().split())) for _ in range(q_N)]

dp = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N - i):
        start = j
        end = start + i

        if start == end:
            dp[start][end] = 1

        elif nums[start] == nums[end]:
            if end == start + 1:
                dp[start][end] = 1
            elif dp[start + 1][end - 1] == 1:
                dp[start][end] = 1

for q in q_arr:
    start, end = q
    print(dp[start-1][end-1])

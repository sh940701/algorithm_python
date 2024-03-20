N = int(input())
arr = list(map(int, input().split()))

memo = [0 for _ in range(N + 1)]

for i in range(N):
    memo[i + 1] = max(memo[i] + arr[i], arr[i])

print(max(memo[1:]))

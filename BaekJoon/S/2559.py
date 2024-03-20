N, K = list(map(int, input().split()))
arr = list(map(int, input().split()))

memo = [0] * (N + 1)

for i in range(N):
    memo[i + 1] = memo[i] + arr[i]

result = float('-inf')

for i in range(K, N + 1):
    result = max(result, memo[i] - memo[i - K])

print(result)

N, target = map(int, input().split())

nums = list(int(input()) for _ in range(N))

result = [0] * (target + 1)

for num in nums:
    for i in range(num, len(result)):
        if num == i:
            result[i] = 1
            continue
        if result[i - num] != 0 and (result[i] == 0 or result[i] > result[i - num] + 1):
            result[i] = result[i - num] + 1

print(result[target]) if result[target] else print(-1)

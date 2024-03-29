N, target = map(int, input().split())

coins = [int(input()) for _ in range(N)]

count = 0

for coin in coins[::-1]:
    if target == 0:
        break
    if coin > target:
        continue

    count += target // coin
    target %= coin

print(count)

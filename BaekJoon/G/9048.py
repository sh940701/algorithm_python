T = int(input())

cases = []

for _ in range(T):
    _N = int(input())
    _coins = list(map(int, input().split()))
    _target = int(input())
    cases.append([_N, _coins, _target])

for case in cases:
    N, coins, target = case

    result = [0] * (target + 1)
    result[0] = 1

    for coin in coins:
        for i in range(coin, len(result)):
            if result[i - coin] != 0:
                result[i] += result[i - coin]

    print(result[target])

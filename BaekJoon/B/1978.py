N = int(input())
arr = list(map(int, input().split()))

result = 0

for n in arr:
    if n == 1:
        continue

    isPrime = True

    for i in range(1, int(n ** 0.5) + 1):
        if i == 1:
            continue
        if n % i == 0:
            isPrime = False

    if isPrime:
        result += 1

print(result)

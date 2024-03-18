import math

N = int(input())
arr = list(int(input()) for _ in range(N))

primes = [True] * (max(arr) + 1)

for num in range(2, int(max(arr) ** 0.5) + 1):
    if primes[num]:
        for i in range(num + num, max(arr) + 1, num):
            primes[i] = False
    # for i in range(2, int(num ** 0.5) + 1):
    #     if num % i == 0:
    #         primes[i] = False
    #         break
    # else:
    #     for i in range(num * 2, len(primes), num):
    #         primes[i] = False

# tmp_arr = []
#
# for i in range(len(primes)):
#     if primes[i]:
#         tmp_arr.append(i)
#
# print(primes)

for case in arr:
    for i in range(math.ceil(case / 2), case + 1):
        if not primes[i]:
            continue
        elif primes[case - i]:
            print(case - i, i)
            break


# print(tmp_arr)

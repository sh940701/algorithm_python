# https://cotak.tistory.com/70

import sys

arr = list(int(sys.stdin.readline()) for _ in range(9))


def combination(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for C in combination(rest_arr, n - 1):
            result.append([elem] + C)

    return result


comb = combination(arr, 7)

for short in comb:
    if sum(short) == 100:
        for num in sorted(short):
            print(num)
        break

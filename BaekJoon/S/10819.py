import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


def permutation(arr, n):
    result = []
    if n > len(arr):
        return result

    elif n == 1:
        for i in arr:
            result.append([i])

    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in permutation(ans, n - 1):
                result.append([arr[i]] + p)

    return result


def calculate(arr):
    result = 0
    for i in range(1, len(arr)):
        result += abs(arr[i] - arr[i - 1])
    return result

perm = permutation(arr, N)

max_result = 0

for case in perm:
    max_result = max(max_result, calculate(case))

print(max_result)

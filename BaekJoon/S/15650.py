N, M = list(map(int, input().split()))


def recur(number, arr):
    results = []
    if number == M:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for result in recur(number + 1, rest_arr):
            results.append([elem] + result)

    return results


arr = [i for i in range(1, N + 1)]

for elem in recur(0, arr):
    print(*elem)

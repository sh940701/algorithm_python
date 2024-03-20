N, M = list(map(int, input().split()))


def recur(number, arr):
    if number == M:
        print(*arr)
        return
    for i in range(1, N + 1):
        if i in arr:
            continue
        arr.append(i)
        recur(number + 1, arr)
        arr.pop()


arr = []
recur(0, arr)

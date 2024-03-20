N, M = list(map(int, input().split()))


def recur(arr: list, n: int) -> None:
    if n == M:
        print(*arr)
        return

    for i in range(1, N + 1):
        if len(arr) > 0 and arr[-1] > i:
            continue
        arr.append(i)
        recur(arr, n + 1)
        arr.pop()


arr = []

recur(arr, 0)

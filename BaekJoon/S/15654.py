N, M = list(map(int, input().split()))
perm = list(map(int, input().split()))

perm.sort()


def recur(arr: list, n: int) -> None:
    global perm

    if n == M:
        print(*arr)
        return

    for item in perm:
        if item in arr:
            continue

        arr.append(item)
        recur(arr, n + 1)
        arr.pop()


arr = []
recur(arr, 0)

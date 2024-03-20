N, M = list(map(int, input().split()))
perm = list(map(int, input().split()))

perm.sort()

visited = []


def recur(arr: list, n: int, excepts: list) -> None:
    global perm

    if n == M:
        print(*arr)
        visited.append(arr[0])
        return

    for idx, item in enumerate(perm):
        if item in visited or item in arr:
            continue
        arr.append(item)
        recur(arr, n + 1, excepts)
        arr.pop()


recur([], 0, [])

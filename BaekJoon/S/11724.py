import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]

mapping = {i: [] for i in range(N + 1)}

for line in graph:
    s, e = line
    mapping.get(s).append(e)
    mapping.get(e).append(s)

visited = set()


def dfs(start):
    if start in visited:
        return

    visited.add(start)
    next_targets = mapping.get(start)

    if next_targets:
        for next_target in next_targets:
            if next_target not in visited:
                dfs(next_target)


answer = 0

for key in range(1, N + 1):
    if key not in visited:
        answer += 1
        dfs(key)

print(answer)

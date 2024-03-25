from collections import deque

N, M, V = list(map(int, input().split()))

graph = [list(map(int, input().split())) for _ in range(M)]

mapping = dict()

dfs_result = []
bfs_result = []

for line in graph:
    s, e = line
    if not mapping.get(s):
        mapping[s] = []
    if not mapping.get(e):
        mapping[e] = []

    mapping[s].append(e)
    mapping[e].append(s)

for key in mapping:
    mapping[key].sort()

visited_dfs = set()


def dfs(start):
    if start in visited_dfs:
        return

    visited_dfs.add(start)
    dfs_result.append(start)
    targets = mapping.get(start)
    if targets:
        for target in targets:
            dfs(target)


dfs(V)
visited_bfs = set()


def bfs(start):
    queue = deque([start])
    visited_bfs.add(start)

    while queue:
        current = queue.popleft()
        bfs_result.append(current)
        targets = mapping.get(current)
        if targets:
            for target in targets:
                if target not in visited_bfs:
                    visited_bfs.add(target)
                    queue.append(target)


bfs(V)

print(*dfs_result)
print(*bfs_result)

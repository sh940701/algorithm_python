N = int(input())
V = int(input())
arr = [list(map(int, input().split())) for _ in range(V)]

mapping = dict()

for line in arr:
    s, e = line

    if not mapping.get(s):
        mapping[s] = []
    if not mapping.get(e):
        mapping[e] = []

    mapping[s].append(e)
    mapping[e].append(s)

visited = set()

answer = 0


def dfs(start):
    global answer

    if start in visited:
        return

    visited.add(start)
    answer += 1

    next_targets = mapping.get(start)
    if next_targets:
        for next_target in next_targets:
            if next_target not in visited:
                dfs(next_target)


dfs(1)

print(answer - 1)  # 1 제외

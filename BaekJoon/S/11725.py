import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 9)

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N - 1)]

mapping = defaultdict(list)
for line in arr:
    s, e = line
    mapping[s].append(e)
    mapping[e].append(s)

parents = [-1] * (N + 1)


def dfs(start):
    next_targets = mapping.get(start)
    if next_targets:
        for next_target in next_targets:

            if parents[next_target] == -1 and next_target != 1:
                parents[next_target] = start
                dfs(next_target)


dfs(1)

for i in range(2, len(parents)):
    print(parents[i])

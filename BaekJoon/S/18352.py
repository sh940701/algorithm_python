import sys
from collections import deque, defaultdict

N, M, K, X = list(map(int, sys.stdin.readline().split()))

arr = [list(map(int, input().split())) for _ in range(M)]

mapping = defaultdict(list)

for line in arr:
    s, e = line
    mapping[s].append(e)

visited = [False] * (N + 1)
distance = [-1] * (N + 1)
distance[X] = 0

results = []


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        current_target = queue.popleft()
        next_targets = mapping.get(current_target)

        if next_targets:
            for next_target in next_targets:
                if not visited[next_target]:
                    visited[next_target] = True
                    queue.append(next_target)
                    distance[next_target] = distance[current_target] + 1


bfs(X)

found = False
for i in range(len(distance)):
    if distance[i] == K:
        found = True
        print(i)

if not found:
    print(-1)

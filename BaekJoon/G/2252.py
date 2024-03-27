from collections import deque

N, M = map(int, input().split())

ingress_count = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

queue = deque()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    ingress_count[b] += 1

for i in range(1, N + 1):
    if ingress_count[i] == 0:
        queue.append(i)

result = []

while queue:
    num = queue.popleft()
    result.append(num)

    for target in graph[num]:
        ingress_count[target] -= 1
        if ingress_count[target] == 0:
            queue.append(target)

print(*result)

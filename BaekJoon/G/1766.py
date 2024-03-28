import heapq

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

ingress_count = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

heap = []

for line in arr:
    a, b = line
    graph[a].append(b)
    ingress_count[b] += 1

for i in range(1, N + 1):
    if ingress_count[i] == 0:
        heapq.heappush(heap, i)

result = []

tmp_arr = []

while heap:

    current = heapq.heappop(heap)
    result.append(current)

    next_targets = graph[current]

    for next_target in next_targets:
        ingress_count[next_target] -= 1
        if ingress_count[next_target] == 0:
            heapq.heappush(heap, next_target)

print(*result)

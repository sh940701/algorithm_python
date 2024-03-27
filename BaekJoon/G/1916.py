import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = list(map(int, input().split()))


def dijkstra(start):
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        cost, now = heapq.heappop(queue)
        if distance[now] < cost:
            continue

        for i in graph[now]:
            next_cost = cost + i[1]
            if next_cost < distance[i[0]]:
                distance[i[0]] = next_cost
                heapq.heappush(queue, (next_cost, i[0]))

    return distance[end]


print(dijkstra(start))

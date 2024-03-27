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
    cost_map = [float('inf')] * (N + 1)
    cost_map[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        current_cost, current_point = heapq.heappop(queue)
        if cost_map[current_point] < current_cost:
            continue

        for next_target, next_cost_from_now in graph[current_point]:
            next_cost_from_root = current_cost + next_cost_from_now
            if next_cost_from_root < cost_map[next_target]:
                cost_map[next_target] = next_cost_from_root
                heapq.heappush(queue, (next_cost_from_root, next_target))

    return cost_map[end]


print(dijkstra(start))

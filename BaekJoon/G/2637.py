import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N = int(input())
M = int(input())

lines = [list(map(int, input().split())) for _ in range(M)]

ingress_count = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

relation_map = defaultdict(list)

cost_map = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for line in lines:
    b, a, cost = line
    graph[a].append((b, cost))
    ingress_count[b] += 1

queue = deque()
root_nodes = []

for i in range(1, N + 1):
    if ingress_count[i] == 0:
        root_nodes.append(i)
        cost_map[i][i] = 1
        queue.append(i)

results = []

while queue:
    current = queue.popleft()
    results.append(current)

    for target in graph[current]:
        next_node, cost = target
        for i in root_nodes:
            if cost_map[current][i] != 0:
                cost_map[next_node][i] += cost_map[current][i] * cost
        ingress_count[next_node] -= 1
        if ingress_count[next_node] == 0:
            queue.append(next_node)

for root in sorted(root_nodes):
    print(root, cost_map[N][root])

print(*cost_map, sep='\n')

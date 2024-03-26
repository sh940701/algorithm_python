import sys

sys.setrecursionlimit(10 ** 9)

k = int(input())


def dfs(start, visited, graph, group):
    visited[start] = group

    for point in graph[start]:
        if visited[point] == 0:
            result = dfs(point, visited, graph, -group)
            if not result:
                return False
        else:
            if visited[point] == group:
                return False

    return True


for _ in range(k):
    V, E = list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        a, b = list(map(int, sys.stdin.readline().split()))
        graph[a].append(b)
        graph[b].append(a)

    result = True
    for i in range(1, V + 1):
        if visited[i] == 0 and dfs(i, visited, graph, -1) == False:
            result = False
            break

    print('YES') if result else print('NO')

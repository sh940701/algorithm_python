from collections import deque

N = int(input())

graph = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

def bfs():
    count = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] != 0:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
                    count += 1

    return count


results = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            graph[i][j] = 0
            queue.append((i, j))
            results.append(bfs() + 1)

print(len(results))
for result in sorted(results):
    print(result)

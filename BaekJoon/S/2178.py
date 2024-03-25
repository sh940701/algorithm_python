from collections import deque

N, M = list(map(int, input().split()))

graph = [list(map(int, input())) for _ in range(N)]

answer = None

graph[0][0] = 0


def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        ex, ey = queue.popleft()

        if ex == N - 1 and ey == M - 1:
            return graph[ex][ey]

        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx, ny = dx + ex, dy + ey
            if -1 < nx < N and -1 < ny < M and graph[nx][ny] == 1:
                graph[nx][ny] += graph[ex][ey]
                queue.append([nx, ny])


bfs(0, 0)
print(graph[N - 1][M - 1] + 1)

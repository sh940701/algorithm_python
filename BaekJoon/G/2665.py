from collections import deque

N = int(input())

mapping = [list(input()) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0, ]

queue = deque()
queue.append((0, 0))

visited = [[float('inf')] * N for _ in range(N)]
visited[0][0] = 0

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if mapping[nx][ny] == '1' and visited[x][y] < visited[nx][ny]:
                visited[nx][ny] = visited[x][y]
                queue.append((nx, ny))
            elif mapping[nx][ny] == '0' and visited[x][y] + 1 < visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

print(visited[N - 1][N - 1])

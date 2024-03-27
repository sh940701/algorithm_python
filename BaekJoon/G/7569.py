import sys
from collections import deque

input = sys.stdin.readline

M, N, H = list(map(int, input().split()))

tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

queue = deque()
visited = [[[-1] * M for _ in range(N)] for _ in range(H)]

for h in range(H):
    for x in range(N):
        for y in range(M):
            if tomatoes[h][x][y] == 1:
                queue.append((h, x, y))
                visited[h][x][y] = 0
            elif tomatoes[h][x][y] == -1:
                visited[h][x][y] = -2

dh = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]

while queue:
    h, x, y = queue.popleft()

    for i in range(6):
        nh, nx, ny = h + dh[i], x + dx[i], y + dy[i]
        if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and tomatoes[nh][nx][ny] == 0:
            visited[nh][nx][ny] = visited[h][x][y] + 1
            tomatoes[nh][nx][ny] = 1
            queue.append((nh, nx, ny))

answer = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if visited[i][j][k] == -1:
                print(-1)
                exit(0)
            answer = max(visited[i][j][k], answer)

print(answer)

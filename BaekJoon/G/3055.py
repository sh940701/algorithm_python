from collections import deque

R, C = map(int, input().split())

mapping = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

queue = deque()

animal_start = None
water_starts = []

for i in range(R):
    for j in range(C):
        if mapping[i][j] == 'S':
            animal_start = ('animal', i, j)
        elif mapping[i][j] == '*':
            water_starts.append(('water', i, j))

for i in water_starts:
    queue.append(i)
queue.append(animal_start)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    type, x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:

            if type == 'water':
                if mapping[nx][ny] != 'D' and mapping[nx][ny] != 'X' and mapping[nx][ny] != '*':
                    queue.append(('water', nx, ny))
                    mapping[nx][ny] = '*'

            if type == 'animal':
                if mapping[nx][ny] == 'D':
                    print(visited[x][y] + 1)
                    exit(0)
                elif mapping[nx][ny] != '*' and mapping[nx][ny] != 'X' and visited[nx][ny] == 0:
                    queue.append(('animal', nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

print('KAKTUS')

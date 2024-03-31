N = int(input())

meetings = [list(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))

current_time = meetings[0][1]
count = 1

for i in range(1, N):
    start, end = meetings[i]
    if current_time <= start:
        count += 1
        current_time = end

print(count)

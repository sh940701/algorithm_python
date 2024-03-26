import sys
from collections import defaultdict

N = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().rstrip()))
routes = [list(map(int, sys.stdin.readline().split())) for _ in range(N - 1)]

mapping = defaultdict(list)

answer = 0

for route in routes:
    s, e = route

    mapping[s].append(e)
    mapping[e].append(s)

    if arr[s] == 1 and arr[e] == 1:
        answer += 2


# def dfs(start, visited: set):
#     global answer
#
#     visited.add(start)
#
#     next_targets = mapping.get(start)
#
#     for next_target in next_targets:
#         if arr[start] == 1 and arr[next_target] == 0 and next_target not in visited:
#             dfs(next_target, visited)
#         elif arr[start] == 0 and arr[next_target] == 0 and next_target not in visited:
#             dfs(next_target, visited)
#         elif arr[start] == 0 and arr[next_target] == 1 and next_target not in visited:
#             answer += 1


def for_inside(start):
    global answer

    near = mapping.get(start)
    count = 0
    for n in near:
        if arr[n] == 1:
            count += 1

    answer += count * (count - 1)


for i in range(1, N + 1):
    if arr[i] == 0:
        for_inside(i)

print(answer)

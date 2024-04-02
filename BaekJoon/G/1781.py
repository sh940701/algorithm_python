import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

problem_map = defaultdict(list)

max_deadline = 0

for _ in range(N):
    deadline, food = list(map(int, input().split()))

    problem_map[deadline].append(food)

    max_deadline = max(max_deadline, deadline)

available_works = []

answer = 0

for time in range(max_deadline, 0, -1):
    while problem_map[time]:
        heapq.heappush(available_works, -problem_map[time].pop())

    if available_works:
        answer += -heapq.heappop(available_works)

print(answer)

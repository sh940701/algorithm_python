from collections import deque

N, K = list(map(int, input().split()))

queue = deque()

for i in range(1, N + 1):
    queue.append(i)

result = []

ptr = 0

while len(queue):
    ptr += 1
    if ptr % K == 0:
        result.append(queue.popleft())
    else:
        queue.append(queue.popleft())

print('<' + ', '.join(str(num) for num in result) + '>')

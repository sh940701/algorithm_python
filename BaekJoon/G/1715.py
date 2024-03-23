import heapq

N = int(input())

arr = list(int(input()) for _ in range(N))

heapq.heapify(arr)

value = 0

while len(arr) > 1:
    value1 = heapq.heappop(arr)
    value2 = heapq.heappop(arr)

    value += value1 + value2
    heapq.heappush(arr, value1 + value2)

print(value)

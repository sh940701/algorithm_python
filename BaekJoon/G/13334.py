import heapq
import sys

N = int(input())

people = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

line_length = int(input())

length_filtered_people = []

for person in people:
    # 포함될 수 있는 길이인지 먼저 filtering
    if abs(person[0] - person[1]) <= line_length:
        # 더 긴 값을 기준으로 오름차순 정렬 되도록 heap 에 push
        heapq.heappush(length_filtered_people, (max(person[0], person[1]), min(person[1], person[0])))

available_heap = []
result = 0

for _ in range(len(length_filtered_people)):
    # 현재 heap 에서 pop 하는 끝 값이 가장 작은 것들 부터임
    end, start = heapq.heappop(length_filtered_people)

    # 방금 꺼낸 값은 end - length 에 start 가 포함되기 때문에 바로 available_heap 에 push
    # 위에서 한번 filtering 을 했기 때문임
    # 이 때 available_heap 에는 start 를 기준으로 오름차순 정렬함
    heapq.heappush(available_heap, (start, end))

    # available_heap 에서 end - line_length 를 기준으로 start 가 해당 값보다 더 작은 요소들을 pop 함
    # start 기준 오름차순으로 넣어줬기 때문에 pop 된 요소들은 start 가 작은 순서
    # 또한 start < end - line_length 에 걸리지 않은 요소들은, (start - end) <= line_length 이기 때문에 현재 end - line_length 범위 내에 포함된다.
    while available_heap and available_heap[0][0] < end - line_length:
        heapq.heappop(available_heap)

    # 그러므로 현재 available_heap 에 남아있는 요소들은 모두 한 line_length 에 포함되는 요소로, result 가 될 수 있음
    result = max(result, len(available_heap))

print(result)

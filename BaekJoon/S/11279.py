from collections import deque


# https://wikidocs.net/194566 -> 최소힙
# heap 을 이용한 priority Queue 구현 -> 최대힙


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, data):
        self.heap.append(data)
        current = len(self.heap) - 1

        while current > 0:
            # 추가한 원소의 부모 인덱스를 구한다.
            parent = (current - 1) // 2
            if self.heap[parent] < self.heap[current]:
                self.heap[parent], self.heap[current] = self.heap[current], self.heap[parent]
                current = parent
            else:
                break

    def pop(self):
        if not self.heap:
            return 0
        elif len(self.heap) == 1:
            return self.heap.pop()

        pop_data, self.heap[0] = self.heap[0], self.heap.pop()
        current, child = 0, 1

        while child < len(self.heap):
            sibling = child + 1
            if sibling < len(self.heap) and self.heap[child] < self.heap[sibling]:
                child = sibling
            if self.heap[current] < self.heap[child]:
                self.heap[current], self.heap[child] = self.heap[child], self.heap[current]
                current = child
                child = current * 2 + 1
            else:
                break
        return pop_data


N = int(input())
arr = list(int(input()) for _ in range(N))

queue = PriorityQueue()

for num in arr:
    if num == 0:
        print(queue.pop())
    else:
        queue.push(num)

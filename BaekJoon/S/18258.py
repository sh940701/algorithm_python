# import sys
#
#
# class Queue:
#     def __init__(self):
#         self.arr = []
#
#     def push(self, value):
#         self.arr.append(value)
#
#     def pop(self):
#         if not len(self.arr):
#             return -1
#         else:
#             value = self.arr[0]
#             self.arr = self.arr[1:]
#             return value
#
#     def size(self):
#         return len(self.arr)
#
#     def empty(self):
#         return int(len(self.arr) == 0)
#
#     def front(self):
#         return self.arr[0] if len(self.arr) else -1
#
#     def back(self):
#         return self.arr[-1] if len(self.arr) else -1
#
#
# N = int(input())
#
# arr = [list(sys.stdin.readline().split()) for _ in range(N)]
#
# queue = Queue()
#
# for operator in arr:
#     if operator[0] == 'push':
#         queue.push(int(operator[1]))
#     elif operator[0] == 'pop':
#         print(queue.pop())
#     elif operator[0] == 'size':
#         print(queue.size())
#     elif operator[0] == 'empty':
#         print(queue.empty())
#     elif operator[0] == 'front':
#         print(queue.front())
#     elif operator[0] == 'back':
#         print(queue.back())

import sys
from collections import deque

N = int(input())

queue = deque()

for _ in range(N):
    operator = list(sys.stdin.readline().split())
    if operator[0] == 'push':
        queue.append(operator[1])
    elif operator[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif operator[0] == 'size':
        print(len(queue))
    elif operator[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif operator[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif operator[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

import sys

N = int(input())

stack = [int(sys.stdin.readline())]

for i in range(1, N):
    height = int(sys.stdin.readline())
    while len(stack) and stack[-1] <= height:
        stack.pop()
    stack.append(height)

print(len(stack))

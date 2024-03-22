_, K = list(map(int, input().split()))
N = list(input())

stack = []

count = K

for num in N:
    while len(stack) and stack[-1] < num and count > 0:
        stack.pop()
        count -= 1

    stack.append(num)

if count:
    for _ in range(count):
        stack.pop()

print(''.join(stack))

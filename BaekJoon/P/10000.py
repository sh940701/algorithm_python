N = int(input())

circles = [list(map(int, input().split())) for _ in range(N)]
for circle in circles:
    circle[0], circle[1] = (circle[0] - circle[1]), (circle[0] + circle[1])
circles.sort(key=lambda x: (x[0], -x[1]))
stack = []

result = 0

for circle in circles:
    if len(stack) == 0:
        stack.extend(circle)
        result += 2
        continue

    tmp_stack = []

    while len(stack) and stack[-1] > circle[0]:
        tmp_stack.append(stack.pop())

    if len(tmp_stack) == 0:
        result += 1
        stack.append(circle[0])
    elif stack[-1] == circle[0] and tmp_stack[-1] > circle[1]:
        result += 1
        stack.extend(circle)
        stack.extend(reversed(tmp_stack))
    elif stack[-1] == circle[0] and tmp_stack[-1] == circle[1]:
        result += 2
        stack.extend(circle)
        stack.extend(reversed(tmp_stack))
    elif stack[-1] < circle[0] and tmp_stack[-1] > circle[1]:
        result += 1
        stack.extend(circle)
        stack.extend(reversed(tmp_stack))
    elif stack[-1] < circle[0] and tmp_stack[-1] == circle[1]:
        result += 1
        stack.extend(circle)
        stack.extend(reversed(tmp_stack))

print(result)

string = input()
bomb = list(input())

stack = []

for s in string:
    stack.append(s)
    if len(stack) >= len(bomb):
        if stack[len(stack) - len(bomb):] == bomb:
            for _ in range(len(bomb)):
                stack.pop()

print(''.join(stack)) if len(stack) else print('FRULA')

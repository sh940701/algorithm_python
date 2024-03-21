brackets = list(input())

result = 0
tmp_result = 1

stack = []

for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append('(')
        tmp_result *= 2

    if brackets[i] == '[':
        stack.append('[')
        tmp_result *= 3

    if brackets[i] == ')':
        if not len(stack) or stack[-1] != '(':
            result = 0
            break
        if brackets[i - 1] == '(':
            result += tmp_result
        tmp_result //= 2
        stack.pop()

    if brackets[i] == ']':
        if not len(stack) or stack[-1] != '[':
            result = 0
            break
        if brackets[i - 1] == '[':
            result += tmp_result
        tmp_result //= 3
        stack.pop()

if len(stack):
    result = 0

print(result)

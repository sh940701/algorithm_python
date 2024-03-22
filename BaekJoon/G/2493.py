N = int(input())
arr = list(map(int, input().split()))

result = [0] * N

stack = []

for idx in range(len(arr))[::-1]:
    while len(stack) and stack[-1][1] <= arr[idx]:
        reachable = stack.pop()
        result[reachable[0]] = idx + 1

    stack.append([idx, arr[idx]])

print(*result)

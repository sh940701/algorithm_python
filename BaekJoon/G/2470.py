N = int(input())
arr = list(map(int, input().split()))

arr.sort()

start = 0
last = N - 1

result = arr[0] + arr[-1]
answer = [arr[0], arr[-1]]

while start < last:
    tmp = arr[start] + arr[last]

    if tmp == 0:
        answer[0], answer[1] = arr[start], arr[last]
        break

    elif abs(result) > abs(tmp):
        result = tmp
        answer[0], answer[1] = arr[start], arr[last]

    if tmp < 0:
        start += 1
    else:
        last -= 1

print(*answer)

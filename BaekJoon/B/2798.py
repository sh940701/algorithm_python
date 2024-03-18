import sys

N, M = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(len(arr)):
    x = arr[i]
    for j in range(i + 1, len(arr)):
        y = arr[j]
        for k in range(j + 1, len(arr)):
            z = arr[k]
            if x + y + z > M:
                continue
            elif x + y + z > result:
                result = x + y + z

print(result)



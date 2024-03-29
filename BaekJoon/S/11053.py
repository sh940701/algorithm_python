N = int(input())
arr = [0] + list(map(int, input().split()))

result = float('-inf')

for i in range(N):
    count = 1
    max_value = arr[i]
    for j in range(i, N):
        if max_value < arr[j]:
            max_value = arr[j]
            count += 1

    result = max(result, count)

print(result)

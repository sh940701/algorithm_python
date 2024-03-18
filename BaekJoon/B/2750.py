N = int(input())
arr = list(int(input()) for _ in range(N))

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

list(map(lambda n: print(n), arr))

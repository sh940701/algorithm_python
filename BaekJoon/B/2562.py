arr = list(int(input()) for _ in range(9))

result = max(arr)

print(max(arr))
print(arr.index(result) + 1)

N = int(input())

result = []

for _ in range(N):
    data = int(input())
    if data == 0:
        result.pop()
    else:
        result.append(data)

print(sum(result))

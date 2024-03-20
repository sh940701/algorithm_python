N = int(input())

count = 0
for i in range(1, N + 1):
    if i ** 2 > N:
        break
    count += 1

print(count)

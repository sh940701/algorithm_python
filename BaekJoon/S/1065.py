N = int(input())

count = 0

for i in range(1, N + 1):
    if i < 100:
        count += 1

    elif 100 <= i < 1000:
        f = i % 10
        s = i // 10 % 10
        t = i // 100 % 10

        if t - s == s - f:
            count += 1

    elif i == 1000:
        break


print(count)

N = int(input())

count = 0

for i in range(N + 1):  # 영훈
    for j in range(N + 1):  # 남규
        for k in range(N + 1):  # 택희
            if i + j + k == N and j >= i + 2 and k % 2 == 0 and i != 0 and j != 0 and k != 0:
                count += 1

print(count)

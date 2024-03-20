N = int(input())
arr = list(int(input()) for _ in range(N))

for num in arr:
    for i in range(2, 1000000 + 1):
        if num % i == 0:
            print('NO')
            break
    else:
        print('YES')

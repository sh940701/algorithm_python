N = int(input())
cases = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    print(cases[i][0] + cases[i][1])

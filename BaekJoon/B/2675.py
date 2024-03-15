N = int(input())

arr = [input().split() for _ in range(N)]

for case in arr:
    for string in case[1]:
        print(string * int(case[0]), end='')
    print()

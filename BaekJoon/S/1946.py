T = int(input())

cases = []

for _ in range(T):
    N = int(input())
    people = [list(map(int, input().split())) for _ in range(N)]
    cases.append(people)

for case in cases:
    case.sort()
    count = 1
    b = case[0][1]
    case.sort(key=lambda x: x[0])

    for i in range(1, len(case)):
        if case[i][1] < b:
            count += 1
            b = case[i][1]

    print(count)


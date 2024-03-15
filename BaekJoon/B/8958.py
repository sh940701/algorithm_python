N = int(input())
arr = [input() for _ in range(N)]


def accumulated(N):
    value = 0
    for i in range(1, N + 1):
        value += i
    return value


for OX in arr:
    Olist = OX.split('X')
    result = 0
    for O in Olist:
        Olength = len(O)
        if Olength == 0: continue

        result += accumulated(len(O))
    print(result)

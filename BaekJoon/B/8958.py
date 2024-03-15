N = int(input())
arr = [input() for _ in range(N)]

for OX in arr:
    Olist = OX.split('X')
    result = 0
    for O in Olist:
        n = len(O)
        if n == 0: continue

        result += (n * (n + 1)) // 2
    print(result)

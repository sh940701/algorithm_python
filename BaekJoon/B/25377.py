N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

maxi = float('inf')

for time in arr:
    arrive, bread = time
    if bread >= arrive:
        maxi = min(bread, maxi)


print(maxi) if maxi != float('inf') else print(-1)


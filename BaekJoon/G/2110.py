N, C = list(map(int, input().split()))

house_map = list(int(input()) for _ in range(N))

house_map.sort()

answer = None

start = 0
last = house_map[-1] - house_map[0]

while start <= last:
    mid = (start + last) // 2

    current = house_map[0]
    cnt = 1
    for i in range(len(house_map)):
        if house_map[i] >= current + mid:
            current = house_map[i]
            cnt += 1

    if cnt >= C:
        answer = mid
        start = mid + 1
    else:
        last = mid - 1

print(answer)

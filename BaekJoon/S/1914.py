#  하노이 탑
# https://mgyo.tistory.com/185
N = int(input())

count = 0
results = []


# 원반 no 개를 x 기둥에서 y 기둥으로 옮김
def move(no: int, x: int, y: int) -> None:
    print(f'no: {no}, x: {x}, y: {y}')
    global results
    global count

    if no > 1:
        move(no - 1, x, 6 - x - y)

    if N <= 20:
        results.append([x, y])
    else:
        count += 1

    if no > 1:
        move(no - 1, 6 - x - y, y)


if N <= 20:
    move(N, 1, 3)
    print(len(results))
    for result in results:
        print(' '.join(map(str, result)))
else:
    print(2 ** N - 1)

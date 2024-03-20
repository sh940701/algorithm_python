import sys

N = int(input())

square_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

exponent = 0

exponent_calc = N

while exponent_calc > 1:
    exponent_calc //= 2
    exponent += 1


def check_if_square(arr, x_start, y_start, x_end, y_end):
    value = arr[x_start][y_start]
    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            if arr[i][j] != value:
                return [False]

    return [True, value]


result_white = 0
result_blue = 0


def divide(arr, x_start, y_start, n):
    global result_white
    global result_blue

    x_end = (x_start + 2 ** n)
    y_end = (y_start + 2 ** n)

    if n == 0:
        if arr[x_start][y_start] == 0:
            result_white += 1
        elif arr[x_start][y_start] == 1:
            result_blue += 1

    elif len(arr) > 1:
        is_square = check_if_square(arr, x_start, y_start, x_end, y_end)
        if is_square[0]:
            if is_square[1] == 0:
                result_white += 1
            elif is_square[1] == 1:
                result_blue += 1
        else:
            divide(arr, x_start, y_start, n - 1)  # first
            divide(arr, x_start, (y_start + y_end) // 2, n - 1)  # second
            divide(arr, (x_start + x_end) // 2, y_start, n - 1)  # third
            divide(arr, (x_start + x_end) // 2, (y_start + y_end) // 2, n - 1)  # fourth


divide(square_map, 0, 0, exponent)

print(result_white)
print(result_blue)

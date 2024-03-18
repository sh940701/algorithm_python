N, R, C = list(map(int, input().split()))

result = 0


def quadrant(N, R, C, r_start, c_start) -> None:
    global result
    # r_end = r_start + 2 ** N - 1
    # c_end = c_start + 2 ** N - 1

    if N == 0:
        return

    r_mid = r_start + (2 ** (N - 1))
    c_mid = c_start + (2 ** (N - 1))

    if R < r_mid and C < c_mid:
        # print('1사분면')
        quadrant(N - 1, R, C, r_start, c_start)
    elif R < r_mid and C >= c_mid:
        result += 2 ** (N * 2 - 2)
        # print('2사분면')
        quadrant(N - 1, R, C, r_start, c_start + 2 ** (N - 1))
    elif R >= r_mid and C < c_mid:
        result += 2 * (2 ** (N * 2 - 2))
        # print('3사분면')
        quadrant(N - 1, R, C, r_start + 2 ** (N - 1), c_start)
    elif R >= r_mid and C >= c_mid:
        result += 3 * (2 ** (N * 2 - 2))
        # print('4사분면')
        quadrant(N - 1, R, C, r_start + 2 ** (N - 1), c_start + 2 ** (N - 1))


quadrant(N, R, C, 0, 0)

print(result)

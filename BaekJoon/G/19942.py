N = int(input())
a, b, c, d = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]

answer = float('inf')
yeong_yang_so = ''


def recur(idx: int, A, B, C, D, E, result_string):
    global answer, yeong_yang_so

    if idx == N:
        if a <= A and b <= B and c <= C and d <= D:
            if E < answer:
                answer = E
                yeong_yang_so = result_string
        return

    # 재료를 사용할 경우
    recur(idx + 1, A + arr[idx][0], B + arr[idx][1], C + arr[idx][2], D + arr[idx][3], E + arr[idx][4],
          result_string + str(idx + 1))

    # 재료를 사용하지 않을 경우
    recur(idx + 1, A, B, C, D, E, result_string)


recur(0, 0, 0, 0, 0, 0, '')

print(answer)
print(yeong_yang_so)

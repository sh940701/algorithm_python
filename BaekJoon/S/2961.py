N = int(input())

ingre = [list(map(int, input().split())) for _ in range(N)]


def recur(idx, dan, zzan, use_count):
    global answer

    if idx == N:
        if use_count == 0:
            return
        answer = min(answer, abs(dan - zzan))
        return

    # 재료를 사용하는 경우
    recur(idx + 1, dan * ingre[idx][0], zzan + ingre[idx][1], use_count + 1)
    # 재료를 사용하지 않는 경우
    recur(idx + 1, dan, zzan, use_count)


answer = float('inf')

recur(0, 1, 0, 0)

print(answer)

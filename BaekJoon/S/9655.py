N = int(input())


# 0 은 상근, 1 은 창영

def recur(person, n):
    # 0 일 경우는 person 에 1을 넣어줌
    recur(1, N - 1)
    recur(1, N - 3)


recur(0, N)

N, K = list(map(int, input().split()))
objects = [list(map(int, input().split())) for _ in range(N)]

result_value = float('-inf')


def recur(idx, weight, value):
    global result_value

    if weight > K:
        return
    elif idx == N:
        result_value = max(result_value, value)
        return

    # 물건을 챙길 때
    recur(idx + 1, weight + objects[idx][0], value + objects[idx][1])
    # 물건을 안 챙길 때
    recur(idx + 1, weight, value)


recur(0, 0, 0)

print(result_value)

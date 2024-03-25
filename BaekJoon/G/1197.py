# https://velog.io/@yoopark/baekjoon-1197
# https://techblog-history-younghunjo1.tistory.com/262

V, E = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(E)]

arr.sort(key=lambda x: x[2])

parents = [0] * (V + 1)
for i in range(1, V + 1):
    parents[i] = i


def get_parent(x):
    if parents[x] == x:
        return x
    parents[x] = get_parent(parents[x])
    return parents[x]


def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def same_parent(a, b):
    return get_parent(a) == get_parent(b)


answer = 0
for a, b, cost in arr:
    if not same_parent(a, b):
        union_parent(a, b)
        answer += cost

print(answer)

N, M = list(map(int, input().split()))
trees = list(map(int, input().split()))

trees.sort()

maxi = 0

s = 0
e = max(trees)


def calc(mid):
    global maxi

    length = 0
    for tree in trees:
        if tree > mid:
            length += tree - mid
            if length >= M:
                maxi = mid
                break

    return length >= M


while s <= e:
    mid = (s + e) // 2

    if calc(mid):
        s = mid + 1
    else:
        e = mid - 1

print(maxi)

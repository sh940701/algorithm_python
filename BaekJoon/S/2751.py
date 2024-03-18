import sys

# 병합정렬
# https://www.daleseo.com/sort-merge/
N = int(input())
arr = [0] * N

for i in range(N):
    arr[i] = int(sys.stdin.readline())


def merge_sort(arr):
    def sort(start, last):
        # 길이가 0 / 1 인 배열은 나눌 필요가 없음
        if last - start < 2:
            return
        mid = (start + last) // 2
        sort(start, mid)
        sort(mid, last)
        # 길이가 2 이상인 배열들만 남음
        merge(start, mid, last)

    def merge(start, mid, last):
        temp = []

        s = start
        m = mid

        while s < mid and m < last:
            if arr[s] < arr[m]:
                temp.append(arr[s])
                s += 1
            else:
                temp.append(arr[m])
                m += 1

        while s < mid:
            temp.append(arr[s])
            s += 1

        while m < last:
            temp.append(arr[m])
            m += 1

        for i in range(start, last):
            arr[i] = temp[i - start]

    return sort(0, len(arr))


merge_sort(arr)

list(map(lambda n: print(n), arr))

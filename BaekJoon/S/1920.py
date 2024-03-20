import math

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()


def find(num):
    start = 0
    last = N - 1
    mid = math.ceil((start + last) / 2)

    while True:
        if N_list[mid] == num:
            return True
        elif start == mid or start == last:
            break
        elif N_list[mid] > num:
            last = mid
            mid = math.floor((start + mid) / 2)
        elif N_list[mid] < num:
            start = mid
            mid = math.ceil((mid + last) / 2)
    return False


for idx, num in enumerate(M_list):
    M_list[idx] = 1 if find(num) else 0

for result in M_list:
    print(result)

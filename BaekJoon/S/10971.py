import sys

N = int(input())

cost_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def recur(arr, n):
    global min_value

    if n == N:
        arr.append(arr[0])
        calc = 0
        for i in range(1, N + 1):
            if cost_map[arr[i - 1]][arr[i]] == 0:
                return

            calc += cost_map[arr[i - 1]][arr[i]]
        arr.pop()
        min_value = min(min_value, calc)
        return

    for i in range(N):
        if i in arr:
            continue
        arr.append(i)
        recur(arr, n + 1)
        arr.pop()


min_value = float('inf')

arr = []
recur(arr, 0)

print(min_value)


#
# import sys
#
# N = int(input())
#
# cost_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
#
# def calculate_cost(start, arr, memo):
#     temp_cost = float('inf')
#
#     state_key = (start, tuple(arr))
#     if state_key in memo:
#         return memo[state_key]
#
#     if len(arr) == 0:
#         if cost_map[start][0] == 0:
#             return float('inf')
#         else:
#             return cost_map[start][0]
#
#     for elem in arr:
#         if cost_map[start][elem] == 0:
#             temp_cost = float('inf')
#         else:
#             rest = arr.copy()
#             rest.remove(elem)
#             calculated = calculate_cost(elem, rest, memo)
#
#             temp_cost = min(temp_cost, cost_map[start][elem] + calculated)
#
#     memo[state_key] = temp_cost
#     return temp_cost
#
#
# result_arr = []
#
# for i in range(N):
#     tmp_arr = []
#
#     for j in range(N):
#         tmp_arr.append(j)
#
#     memo = dict()
#
#     result_arr.append(calculate_cost(i, tmp_arr, memo))
#
# print(result_arr)

# (0, [0, 1, 2, 3])
# (1, [1, 2, 3])
# (2, [2, 3])
# (3, [3])
# (3, [2, 3])
# (2, [2])
# (2, [1, 2, 3])
# (1, [1, 3])
# (3, [3])
# (3, [1, 3])
# (1, [1])
# (3, [1, 2, 3])
# (1, [1, 2])
# (2, [2])
# (2, [1, 2])
# (1, [1])

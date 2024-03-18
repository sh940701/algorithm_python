import sys

N = int(input())

cost_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def permutation(arr, n):
    result = []
    if n > len(arr):
        return result

    elif n == 1:
        for i in arr:
            result.append([i])

    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in permutation(ans, n - 1):
                result.append([arr[i]] + p)

    return result


arr = []

for i in range(1, N):
    arr.append(i)

calculated = permutation(arr, N - 1)

# print(calculated)

max_value = float('inf')

for case in calculated:
    case = [0] + case + [0]
    calc = 0
    for i in range(1, N + 1):
        if cost_map[case[i - 1]][case[i]] == 0:
            break
        calc += cost_map[case[i - 1]][case[i]]
    else:
        max_value = min(calc, max_value)

print(max_value)

# import sys
#
# N = int(input())
#
# cost_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# memo = dict()
#
#
# def calculate_cost(start, arr):
#     global memo
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
#             calculated = calculate_cost(elem, rest)
#
#             if calculated == float('inf'):
#                 temp_cost = float('inf')
#             else:
#                 temp_cost = min(temp_cost, cost_map[start][elem] + calculated)
#
#     memo[state_key] = temp_cost
#     return temp_cost
#
#
# tmp_arr = []
#
# for i in range(1, N):
#     tmp_arr.append(i)
#
# print(calculate_cost(0, tmp_arr))

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

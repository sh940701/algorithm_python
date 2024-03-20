import itertools

N = int(input())
nums = list(map(int, input().split()))
operators_count = list(map(int, input().split()))

operators = []

for idx in range(len(operators_count)):
    operator = operators_count[idx]
    while operator > 0:
        operators.append(idx)
        operator -= 1


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


min_value = float('inf')
max_value = float('-inf')

operators_perm = itertools.permutations(operators, N - 1)

for operator_arr in operators_perm:
    result = nums[0]
    for i in range(0, len(nums) - 1):
        if operator_arr[i] == 0:
            result += nums[i + 1]
        elif operator_arr[i] == 1:
            result -= nums[i + 1]
        elif operator_arr[i] == 2:
            result *= nums[i + 1]
        elif operator_arr[i] == 3:
            if result < 0 < nums[i + 1]:
                result = -(abs(result) // nums[i + 1])
            else:
                result //= nums[i + 1]

    min_value = min(min_value, result)
    max_value = max(max_value, result)

print(max_value)
print(min_value)

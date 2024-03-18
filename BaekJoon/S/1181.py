import sys

N = int(input())

arr = list(sys.stdin.readline().strip() for _ in range(N))

result_arr = []

for _ in range(51):
    result_arr.append(set())

for word in arr:
    result_arr[len(word)].add(word)

for result in result_arr:
    if len(result) == 0:
        continue
    result = list(result)
    result.sort()
    for word in result:
        print(word)
ooo

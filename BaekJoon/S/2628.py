X, Y = list(map(int, input().split()))
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

x_arr = [0]
y_arr = [0]

for line in arr:
    if line[0] == 0:
        x_arr.append(line[1])
    else:
        y_arr.append(line[1])

x_arr.sort()
y_arr.sort()

x_arr.append(Y)
y_arr.append(X)

x_max = 0
y_max = 0

for i in range(len(x_arr) - 1):
    x_max = max(x_max, x_arr[i + 1] - x_arr[i])

for i in range(len(y_arr) - 1):
    y_max = max(y_max, y_arr[i + 1] - y_arr[i])

print(x_max * y_max)

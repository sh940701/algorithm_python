A = int(input())
B = int(input())
tmp_B = B

result = 0

for i in range(3):
    x = A * (tmp_B % 10)
    tmp_B = tmp_B // 10
    print(x)
    result += x * (10 ** i)
print(result)

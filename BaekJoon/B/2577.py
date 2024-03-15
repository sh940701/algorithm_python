arr = list(int(input()) for _ in range(3))

calculated = 1

for x in arr:
    calculated *= x

str_calculated = str(calculated)

for i in range(10):
    print(str_calculated.count(str(i)))

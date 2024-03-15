import sys

year = int(input())

result = None

if year % 400 == 0:
    print(1)
    sys.exit()

if year % 100 == 0:
    print(0)
    sys.exit()

if year % 4 == 0:
    print(1)
    sys.exit()

print(0)

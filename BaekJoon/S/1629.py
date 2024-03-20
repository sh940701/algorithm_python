A, B, C = list(map(int, input().split()))


# (7 ** 4) % 13 = ((7 ** 2) % 13 * (7 ** 2) % 13) % 13 = ((7 % 13) * (7 % 13) * (7 % 13) * (7 % 13)) % 13

def mod(a, b, c):
    if b == 1:
        return a % c

    if b % 2 == 0:
        return (mod(a, b // 2, c) ** 2) % c
    else:
        return ((mod(a, b // 2, c) ** 2) * a) % c


print(mod(A, B, C))

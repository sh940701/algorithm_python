A, B = list(map(int, input().split()))

answer = [0] * 2

minimum = float('inf')

mul = A * B

# 구하고자 하는 수는, 두 개 다 A 를 최대공약수로 가지고, 곱해서 B 가 나오는 수이다.
# A * B 의 약수 중 A 의 배수인 것을 구하면 됨
for i in range(A, int(mul ** 0.5) + 1, A):
    if mul % i == 0:
        if i + (mul // i) < minimum:
            a = i
            b = mul // i

            while a % b != 0:
                tmp = a % b
                a = b
                b = tmp

            if b == A:
                minimum = i + mul // i
                answer[0] = min(i, mul // i)
                answer[1] = max(i, mul // i)


print(*answer)

target = list(input())
N = int(input())
words = [input() for _ in range(N)]

# 초기값 세팅을 위해 길이를 하나 늘리고 맨 앞 요소의 값을 1로 바꿔줌
dp = [0] * (len(target) + 1)
dp[0] = 1

for i in range(1, len(dp)):
    for word in words:
        if len(word) <= i and dp[i - len(word)] == 1 and target[i - len(word): i] == list(word):
            dp[i] = 1
            break

print(dp[-1])

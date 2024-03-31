import sys

input = sys.stdin.readline

str1 = [''] + list(input().rstrip())
str2 = [''] + list(input().rstrip())

dp = [["" for _ in range(len(str2))] for _ in range(len(str1))]

for i in range(1, len(str1)):
    x = str1[i]
    for j in range(1, len(str2)):
        y = str2[j]

        if x == y:
            dp[i][j] = dp[i - 1][j - 1] + y

        else:
            if len(dp[i - 1][j]) <= len(dp[i][j - 1]):
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

result = dp[-1][-1]
print(len(result), result, sep='\n')

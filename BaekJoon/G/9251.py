str1 = input()
str2 = input()

dp = [["" for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    x = str1[i - 1]
    for j in range(1, len(str2) + 1):
        y = str2[j - 1]

        if x == y:
            dp[i][j] = dp[i - 1][j - 1] + y

        else:
            if len(dp[i - 1][j]) <= len(dp[i][j - 1]):
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

print(len(dp[len(str1)][len(str2)]))

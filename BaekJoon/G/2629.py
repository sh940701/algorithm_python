N = int(input())
weights = list(map(int, input().split()))
BEAN_N = int(input())
beads = list(map(int, input().split()))

dp = [[0 for _ in range(500 * j + 1)] for j in range(N + 1)]
ans = []


# 추 N 개를 가지고 만들 수 있는 모든 경우의 수를 계산
def cal(num, weight):
    if dp[num][weight] == 1:
        return
    dp[num][weight] = 1  # 추 num 개 째에 도달했을 때 weight 을 만들 수 있는지 여부
    if num == N:
        return

    cal(num + 1, weight + weights[num])
    cal(num + 1, weight)
    cal(num + 1, abs(weight - weights[num]))


cal(0, 0)

for bead in beads:
    if bead > 500 * N:
        ans.append('N')
    elif dp[N][bead] == 1:
        ans.append('Y')
    else:
        ans.append('N')
# print(*dp, sep='\n')
# print(len(dp))
print(*ans)

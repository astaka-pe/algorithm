import math

N = int(input())
c = [[0]*(N+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(N+1):
        c[i][j] = int(input())

dp = [math.inf]*(N+1)
dp[0] = 0

for i in range(N+1):
    for j in range(i):
        dp[i] = min(dp[i], dp[j] + c[j][i])

print(dp[N])
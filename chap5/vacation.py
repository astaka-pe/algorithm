import numpy as np

N = int(input())
a = [0]*N
b = [0]*N
c = [0]*N

for i in range(N):
    a[i], b[i], c[i] = map(int, input().split())

dp = [[0]*(N+1)]*3
dp = np.array(dp)

for i in range(N):
    dp[1][i+1] = max(dp[1][i+1], dp[0][i]+b[i])
    dp[2][i+1] = max(dp[2][i+1], dp[0][i]+c[i])
    dp[0][i+1] = max(dp[0][i+1], dp[1][i]+a[i])
    dp[2][i+1] = max(dp[2][i+1], dp[1][i]+c[i])
    dp[0][i+1] = max(dp[0][i+1], dp[2][i]+a[i])
    dp[1][i+1] = max(dp[1][i+1], dp[2][i]+b[i])

print(max(max(dp[0][N], dp[1][N]), dp[2][N]))
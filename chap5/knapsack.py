import numpy as np

N, W = map(int, input().split())
weight = list(map(int, input().split()))
value = list(map(int, input().split()))
dp = [[0]*(W+1)]*(N+1)
dp = np.array(dp)
for i in range(N):
    for w in range(W+1):
        if w - weight[i] >= 0:
            dp[i+1][w] = max(dp[i+1][w],dp[i][w - weight[i]] + value[i])
        dp[i+1][w] = max(dp[i+1][w],dp[i][w])
    print(np.array(dp))

print(dp[N][W])
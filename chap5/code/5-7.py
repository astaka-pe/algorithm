N, W = map(int, input().split())
weight = [0]*N
value = [0]*N
for i in range(N):
    weight[i], value[i] = map(int, input().split())

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(N):
    for w in range(W+1):
        if w - weight[i] >= 0:
            dp[i+1][w] = max(dp[i+1][w], dp[i][w - weight[i]] + value[i])
        dp[i+1][w] = max(dp[i+1][w], dp[i][w])

print(dp[N][W])
import math
INF = 2**60
N,K = map(int, input().split())
h = list(map(int, input().split()))
dp = [INF] * N
dp[0] = 0

for i in range(N):
    for j in range(1,K+1):
        #配る遷移形式（iからi+jへ）
        if i+j<N:
            dp[i+j] = min(dp[i+j], dp[i]+abs(h[i]-h[i+j]))

print(dp[N-1])

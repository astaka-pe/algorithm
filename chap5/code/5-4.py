import math

N = int(input())
h = list(map(int, input().split()))
dp = [math.inf]*N
dp[0] = 0

for i in range(N):
    if i+1 < N:
        dp[i+1] = min(dp[i+1], dp[i] + abs(h[i] - h[i+1]))
    if i+2 < N:
        dp[i+2] = min(dp[i+2], dp[i] + abs(h[i] - h[i+2]))
        
print(dp[N-1])
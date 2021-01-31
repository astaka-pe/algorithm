import math
N = int(input())
h = list(map(int, input().split()))
dp = [math.inf] * N
dp[0] = 0

for i in range(1,N):
    dp[i] = min(dp[i], dp[i-1]+abs(h[i]-h[i-1]))
    if(i>=2):
        dp[i] = min(dp[i], dp[i-2]+abs(h[i]-h[i-2]))

print(dp[N-1])
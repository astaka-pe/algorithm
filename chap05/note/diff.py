import numpy as np
import math

S, T = input().split()
dp = [[math.inf] * (len(T)+1)] * (len(S)+1)
dp = np.array(dp)
dp[0][0] = 0
for i in range(len(S)+1):
    for j in range(len(T)+1):
        if i>=1 and j>=1:
            if S[i-1] == T[j-1]:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)
        if i>=1:
            dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
        if j>=1:
            dp[i][j] = min(dp[i][j], dp[i][j-1]+1)

print(dp)
print(dp[len(S)][len(T)])
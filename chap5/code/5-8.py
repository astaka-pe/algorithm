import math

S, T = map(str, input().split())
dp = [[math.inf]*(len(T)+1) for _ in range(len(S)+1)]
dp[0][0] = 0

for i in range(len(S)+1):
    for j in range(len(T)+1):
        # change
        if i > 0 and j > 0:
            if S[i-1] == T[j-1]:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + 1)
        # remove
        if i > 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
        # insert
        if j > 0:
            dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)

print(dp[len(S)][len(T)])
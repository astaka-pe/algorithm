import math

def rec(i, dp):
    if dp[i] < math.inf:
        return dp[i]
    if i == 0:
        return 0
    res = math.inf
    res = min(res, rec(i-1, dp) + abs(h[i] - h[i-1]))
    if i > 1:
        res = min(res, rec(i-2, dp) + abs(h[i] - h[i-2]))
    dp[i] = res
    return res

N = int(input())
h = list(map(int, input().split()))
dp = [math.inf]*N

print(rec(N-1, dp))
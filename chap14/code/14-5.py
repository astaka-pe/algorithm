import numpy as np
# フロイド・ワーシャル法の実装
INF = 2**60

# 頂点数，辺数
N, M = map(int, input().split())

# dp配列
dp = [[INF]*N for _ in range(N)]
dp = np.asarray(dp)
# dp初期条件
for e in range(M):
    a, b, w = map(int, input().split())
    dp[a][b] = w
for v in range(N):
    dp[v][v] = 0

# dp遷移
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
# 結果出力
# もしdp[v][v]<0なら負閉路が存在
exist_negative_cycle = False
for v in range(N):
    if dp[v][v] < 0:
        exist_negative_cycle = True
if exist_negative_cycle:
    print("NEGATIVE CYCLE")
else:
    for i in range(N):
        for j in range(N):
            if dp[i][j] >= INF/2:
                dp[i][j] = -1
    print(dp)
"""
6 9
0 1 3
0 2 5
1 2 4
1 3 12
2 3 9
2 4 4
4 3 7
4 5 8
3 5 2
"""


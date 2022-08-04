# 単純なダイクストラ法の実装
INF = 2**60

# グラフを入力として受け取る
N, M, s = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b, w = map(int, input().split())
    G[a].append([b,w]) #有向グラフ

# ダイクストラ法
used = [False]*N
dist = [INF]*N
dist[s] = 0
for iter in range(N):
    # 使用済みでない頂点のうち，distが最小の頂点を探す
    min_dist = INF
    min_v = -1
    for v in range(N):
        if used[v]==False and dist[v] < min_dist:
            min_dist = dist[v]
            min_v = v
    # もしそのような頂点が見つからなければ終了する
    if min_v == -1:
        break
    # min_vを始点とした各辺を緩和
    for e in G[min_v]:
        to = e[0] # 到達先頂点
        w = e[1] # 重み
        if dist[to] > dist[min_v]+w:
            dist[to] = dist[min_v]+w
    used[min_v] = True

for v in range(N):
    if dist[v]<INF:
        print(dist[v])
    else:
        print("INF")

"""
6 9 0
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


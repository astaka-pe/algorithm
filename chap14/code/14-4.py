# ヒープを用いるダイクストラ法の実装
import heapq
INF = 2**60

# グラフを入力として受け取る
N, M, s = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b, w = map(int, input().split())
    G[a].append([b,w]) #有向グラフ

# ダイクストラ法
dist = [INF]*N
dist[s] = 0
que = []
heapq.heappush(que, (dist[s], s))

while len(que)!= 0:
    # v:使用済みでない頂点のうち，d[v]が最小の頂点
    # d:vに対するキー値
    d, v = heapq.heappop(que)
    # d > dist[v]は(d,v)がゴミであることを意味する
    if d > dist[v]:
        continue
    # vを始点とした各辺を緩和
    for e in G[v]:
        to = e[0] # 到達先頂点
        w = e[1] # 重み
        if dist[to] > dist[v]+w:
            dist[to] = dist[v]+w
            # 更新があるならヒープに挿入
            heapq.heappush(que, (dist[to], to))

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


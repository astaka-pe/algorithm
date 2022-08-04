# ベルマン・フォード法の実装
INF = 2**60

# グラフを入力として受け取る
N, M, s = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b, w = map(int, input().split())
    G[a].append([b,w]) #有向グラフ

# ベルマン・フォード法
exist_negative_cycle = False
dist = [INF]*N
dist[s] = 0
for iter in range(N):
    update = False # 更新が発生したかどうか
    for v in range(N):
        # dist[v]=INFのときはvからの緩和を行わない
        if dist[v] == INF:
            continue
        for e in G[v]:
            to = e[0] # 到達先頂点
            w = e[1] # 重み
            if dist[to] > dist[v]+w:
                dist[to] = dist[v]+w
                update = True
    # 更新がなければ既に最短路が求められている
    if update == False:
        break
    # N回目の反復で更新が行われたならば，負経路を持つ
    if iter == N-1 and update:
        exist_negative_cycle = True

if exist_negative_cycle:
    print("NEGATIVE CYCLE")
else:
    for v in range(N):
        if dist[v]<INF:
            print(dist[v])
        else:
            print("INF")

"""
6 12 0
0 1 3
0 3 100
1 3 57
3 1 -5
1 2 50
1 4 -4
2 3 -10
2 4 -5
4 3 25
4 2 57
2 5 100
4 5 8
"""


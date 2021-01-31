# 頂点sから各頂点への最短路長を表す配列
def BFS(G, s):
    N = len(G)          #グラフの頂点数

    # グラフ探索のためのデータ構造
    dist = [-1] * N  # 全頂点を「未訪問」に初期化
    que = []           # 空の状態
    
    # 初期条件
    dist[0] = 0      # sは探索済み
    que.append(0)      # queはsのみを含む

    # queが空になるまで探索を行う
    while len(que)!=0:
        # queから頂点を取り出す
        v = que.pop(0) # 幅優先探索

        # vから辿れる頂点を全て調べる
        for x in G[v]:
            # 発見済みの頂点は探索しない
            if dist[x] != -1:
                continue
            # 新たな頂点xを探索済みとしてqueに挿入
            dist[x] = dist[v]+1
            que.append(x)
        print(que)
    return dist

# グラフを入力として受け取る
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a) #無向グラフ
dist = BFS(G,0)
print(dist)
"""
9 13
0 1
0 4
0 2
1 4
1 3
1 8
4 8
2 5
3 8
8 5
3 7
5 6
7 6
"""
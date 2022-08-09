# 二部グラフ判定
def dfs(G, v, cur=0):
    color[v] = cur
    for next_v in G[v]:
        # 隣接頂点がすでに色確定していた場合
        if color[next_v] != -1:
            # 同じ色が隣接した場合は二部グラフではない
            if color[next_v] == cur:
                return False    # 探索中に二部グラフでないことが判明したらそこで打ち切る
            continue
        # 隣接頂点の色を変えて再帰的に探索
        if dfs(G, next_v, 1-cur) == False:
            return False
    return True


# グラフを入力として受け取る
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b) 
    G[b].append(a) #無向グラフ

general = True
color = [-1]*N
if general:
    """
    本に書いてあるのはこちら（冗長な気がする）
    一般的なグラフ（非接続グラフ）では有効？
    """
    is_bipartite = True
    for v in range(N):
        if color[v] != -1:
            continue
        # 頂点vの色が決まっていない場合 -> 探索中に二部グラフでないことが判明している
        # 頂点vを0で塗って塗れなくなるまで隣接を探索（必ず途中でFalseになるはず）
        # 接続グラフでは冗長（塗れない頂点が0で塗られるだけ）
        if dfs(G, v) == False:
            is_bipartite = False
    print(color)

else:
    """
    接続グラフでは頂点0スタートのDFSで十分
    """
    is_bipartite = dfs(G, 0)
    print(color)

if is_bipartite:
    print("Yes")
else:
    print("No")

"""
9 11
0 1
0 4
0 2
1 3
1 8
4 8
2 5
8 5
3 7
7 6
5 6
"""
"""
5 5
1 0
1 2
1 4
0 3
4 3
"""
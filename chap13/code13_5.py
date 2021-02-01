# 二部グラフ判定
def dfs(G, v, cur=0):
    color[v] = cur
    for next_v in G[v]:
        # 隣接頂点がすでに色確定していた場合
        if color[next_v] != -1:
            # 同じ色が隣接した場合は二部グラフではない
            if color[next_v] == cur:
                return False
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

color = [-1]*N
is_bipartite = True
for v in range(N):
    if color[v] != -1:
        continue
    if dfs(G, v) == False:
        is_bipartite = False
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
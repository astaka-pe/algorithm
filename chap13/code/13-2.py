# 深さ優先探索
def dfs(G, v):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v)


# グラフを入力として受け取る
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b) #有向グラフ

seen = [False]*N
for v in range(N):
    print(seen)
    if seen[v]:
        continue
    dfs(G, v)

# 連結の無向グラフの場合、dfs[G, 0]だけで全頂点が探索済になる

"""
8 12
4 2
4 6
4 1
1 6
6 7
1 3
2 7
3 7
2 5
7 0
3 0
0 5
"""
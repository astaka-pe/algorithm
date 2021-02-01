# s-tパスがあるかどうかを深さ優先探索を用いて判定
def dfs(G, v):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v)


# グラフを入力として受け取る
N, M, s, t = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b) #有向グラフ

seen = [False]*N
dfs(G, s)
if seen[t]:
    print("Yes")
else:
    print("No")

"""
8 12 6 5
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
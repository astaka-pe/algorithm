N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    # 無効グラフの場合
    # G[b].append(a)

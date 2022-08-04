# 重み付きグラフの実装
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b, w = map(int, input().split())
    G[a].append([b,w])
    #G[b].append(a) #無向グラフ
print(G)

"""
入力例
6 9
0 1 5
0 2 2
1 3 4
2 1 8
1 4 2
2 4 7
3 4 6
4 5 1
3 5 3
"""
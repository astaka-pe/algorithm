# v: 現在探索中の頂点、p: vの親（vが根の時は-1）、d: vの深さ
def dfs(G, depth, subtree_size, v, p=-1, d=0):
    depth[v] = d
    subtree_size[v] = 1 # 自分自身
    for c in G[v]:
        if c == p:
            continue    # 親方向への探索を防ぐ

        # vの子cの深さを調べる（行きがけ）
        dfs(G, depth, subtree_size, c, v, d+1)
        # cの親vの部分木サイズを足す（帰りがけ）
        subtree_size[v] += subtree_size[c]  

N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

root = 0
depth = [0]*N
subtree_size = [0]*N
dfs(G, depth, subtree_size, root)

print(depth)
print(subtree_size)

"""図13.14
15
0 1
1 2
1 3
0 4
4 5
5 6
5 7
4 8
8 9
8 10
0 11
11 12
11 13
13 14
"""
# v: 現在探索中の頂点、p: vの親（vが根の時は-1）、d: vの深さ
def dfs(G, depth, v, p=-1, d=0):
    depth[v] = d
    for c in G[v]:
        if c == p:
            continue    # 親方向への探索を防ぐ
        dfs(G, depth, c, v, d+1)
# v: 現在探索中の頂点、p: vの親（vが根の時は-1）
def dfs(G, v, p=-1):
    for c in G[v]:
        if c == p:
            continue    # 親方向への探索を防ぐ
        dfs(G, c, v)
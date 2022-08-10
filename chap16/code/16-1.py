import math

class Edge:
    def __init__(self, r, f, t, c):
        """
        rev: 逆辺(to, fro)がG[to]の中で何番目の要素か
        cap: 辺(from, to)の容量
        """
        self.rev = r
        self.fro = f
        self.to = t
        self.cap = c

class Graph:
    def __init__(self, n):
        self.glist = [[] for _ in range(n)]
        self.size = n

    def redge(self, e):
        return self.glist[e.to][e.rev]
    
    def run_flow(self, e, f):
        e.cap -= f
        self.redge(e).cap += f
    
    def addedge(self, fro, to, cap):
        """
        fromからtoへ容量capの辺を張る
        toからfromへ容量0の辺も張る
        """
        fromrev = len(self.glist[fro])
        torev = len(self.glist[to])
        self.glist[fro].append(Edge(torev, fromrev, to, cap))
        self.glist[to].append(Edge(fromrev, to, fro, 0))

class FordFulkerson:
    def __init__(self):
        self.seen = []
    
    def fodfs(self, G, v, t, f):
        """
        残余グラフ上でs-tパスを見つける
        s-tパス上の容量の最小値を返す（なければ0）
        f: sからvへ到達した過程の各辺の容量の最小値
        """
        # 終端tに達したらリターン
        if v == t:
            return f
        
        # dfs
        self.seen[v] = True
        for e in G.glist[v]:
            if self.seen[e.to]:
                continue
            if e.cap == 0:
                continue
            flow = self.fodfs(G, e.to, t, min(f, e.cap))
            if flow == 0:
                continue
            G.run_flow(e, flow)
            return flow
        return 0
    
    def solve(self, G, s, t):
        res = 0
        while True:
            self.seen = [False]*G.size
            flow = self.fodfs(G, s, t, math.inf)

            if flow == 0:
                return res
            res += flow
        return 0

N, M = map(int, input().split())
G = Graph(N)
for i in range(M):
    a, b, c = map(int, input().split())
    G.addedge(a, b, c)

ff = FordFulkerson()
s = 0
t = N - 1
print(ff.solve(G, s, t))
"""
6 7 
0 1 10
0 3 4
1 2 9
1 4 6
2 5 8
3 4 3
4 5 4
"""

"""
6 9
0 1 5
0 3 5
1 3 37
1 2 4
3 2 3
3 4 9
2 4 56
2 5 9
4 5 2

ans = 9
"""
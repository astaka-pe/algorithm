class Edge:
    def __init__(self, to, w):
        self.to = to
        self.w = w

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b, w = map(int, input().split())
    edge = Edge(b, w)
    G[a].append(edge)
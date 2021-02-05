class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):  # 要素xが属するグループの根を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y): #要素xとyが属するグループを併合
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x): #要素xが属するグループの要素数を返す
        return -self.parents[self.find(x)]

    def same(self, x, y): #要素x,yが同じグループに属するかを返す
        return self.find(x) == self.find(y)

    def members(self, x): #要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self): #全ての根の要素をリストで返す
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self): #グループの数を返す
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

# クラスカル法の実装

N, M = map(int, input().split())
edges = [0]*M
for i in range(M):
    u, v, w = map(int, input().split())
    edges[i] = (w, (u,v)) #有向グラフ]
# 辺の重みが小さい順にソート
edges = sorted(edges)

# クラスカル法
res = 0
uf = UnionFind(N)
for i in range(M):
    w = edges[i][0]
    u = edges[i][1][0]
    v = edges[i][1][1]

    # サイクルが形成される時は追加しない
    if uf.same(u,v):
        continue
    # 辺u,vを追加
    res += w
    uf.union(u,v)
print(res)

"""
6 9
0 1 3
0 2 5
1 2 4
1 3 12
2 3 9
2 4 4
4 3 7
4 5 8
3 5 2
"""
"""
8 12
4 2 9
4 6 2
4 1 4
1 6 3
6 7 7
1 3 8
2 7 5
3 7 6
2 5 10
7 0 3
3 0 5
0 5 6

res=31
"""
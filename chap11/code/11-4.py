class UnionFind:
    def __init__(self, n):
        self.par = [-1]*n
        self.siz = [1]*n
    
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
    
    def issame(self, x, y):
        return self.root(x) == self.root(y)
    
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False

        if self.siz[x] < self.siz[y]:
            x, y = y, x
        
        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True
    
    def size(self, x):
        return self.siz[self.root(x)]

N, M = map(int, input().split())
uf = UnionFind(N)
for i in range(M):
    a, b = map(int, input().split())
    uf.unite(a, b)

res = 0
for x in range(N):
    print("root of {}: {}".format(x, uf.root(x)))
    if uf.root(x) == x:
        res += 1
print(res)

"""
input
7 4
1 2
2 3
5 6
1 6

output
3
"""
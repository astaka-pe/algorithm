N = int(input())
G = [[] for _ in range(N)]
edge = []
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
    edge.append((a,b))

# 深さを求めるDFS
depth = [-1] * N
def DepthDFS(a, d):
    depth[a] = d
    for x in G[a]:
        if depth[x] == -1:
            DepthDFS(x, d+1)
    return depth

# 深さを求めるBFS
depth = [-1] * N
que = []
def DepthBFS(a, d):
    depth[a] = d
    que.append(a)
    while que:
        v = que.pop()
        for x in G[v]:
            if depth[x] != -1:
                continue
            depth[x] = depth[v] + 1
            que.append(x)
    return depth
print(DepthDFS(0,0))
print(DepthBFS(0,0))

"""
11
2 1
1 3
3 4
5 2
1 6
1 7
5 8
3 9
3 10
11 4
"""
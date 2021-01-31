# グラフGにおいて，頂点sを始点とした探索を行う
def search(G, s):
    N = len(G)          #グラフの頂点数

    # グラフ探索のためのデータ構造
    seen = [False] * N  # 全頂点を「未訪問」に初期化
    todo = []           # 空の状態
    
    # 初期条件
    seen[s] = True      # sは探索済み
    todo.append(s)      # todoはsのみを含む

    # todoが空になるまで探索を行う
    while len(todo)!=0:
        # todoから頂点を取り出す
        v = todo.pop(0) # 幅優先探索
        #v = todo.pop(-1)# 深さ優先探索

        # vから辿れる頂点を全て調べる
        for x in G[v]:
            # 発見済みの頂点は探索しない
            if seen[x]:
                continue
            # 新たな頂点xを探索済みとしてtodoに挿入
            seen[x] = True
            todo.append(x)
        print(seen,todo)

# グラフを入力として受け取る
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a) #無向グラフ
search(G,0)

"""
9 11
0 1
0 4
0 2
1 3
1 8
4 8
2 5
8 5
3 7
7 6
5 6
"""


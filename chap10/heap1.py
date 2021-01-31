import heapq
a = [19,12,15,10,7,6,1,3,7,5,3,2]
a = [-1*i for i in a] #最大値を取り出す場合
heapq.heapify(a) #リストをヒープに変換
print(a)
"""
heapq.heappush(a,-17) #プッシュ
print(a)
"""
heapq.heappop(a)
a = [-1*i for i in a]
print(a)

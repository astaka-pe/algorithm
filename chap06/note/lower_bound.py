import bisect
import math

N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b = sorted(b)
min_value = math.inf
for i in range(N):
    index = bisect.bisect_left(b,K-a[i])
    if(index < N):
        if(a[i]+b[index]<min_value):
            min_value = a[i] + b[index]
print(min_value)
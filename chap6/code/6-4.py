import math
import bisect
"""
lower_bound(C++) -> bisect_left(Python)
upper_bound(C++) -> bisect_right(Python)
"""

N, K = map(int, input().split())
a = [0]*N
b = [0]*N

for i in range(N):
    a[i], b[i] = map(int, input().split())

min_value = math.inf

b = sorted(b)
b.append(math.inf)

for i in range(N):
    iter = bisect.bisect_left(b, K - a[i])
    val = b[iter]
    if a[i] + val < min_value:
        min_value = a[i] + val

print(min_value)
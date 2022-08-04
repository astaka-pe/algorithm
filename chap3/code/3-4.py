import math

N, K = map(int, input().split())
a = [0]*N
b = [0]*N
for i in range(N):
    a[i], b[i] = map(int, input().split())

min_value = math.inf

for i in range(N):
    for j in range(N):
        if a[i] + b[j] < K:
            continue
        if a[i] + b[j] < min_value:
            min_value = a[i] + b[j]

print(min_value)
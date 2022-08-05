import math

N = int(input())
a = list(map(int, input().split()))

min_value = math.inf

for i in range(N):
    if a[i] < min_value:
        min_value = a[i]

print(min_value)
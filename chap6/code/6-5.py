import math

N = int(input())
H = [0]*N
S = [0]*N
for i in range(N):
    H[i], S[i] = map(int, input().split())

left = 0
right = math.inf

while right - left > 1:
    mid = (left + right) // 2
    ok = True
    t = [0]*N
    for i in range(N):
        if(mid < H[i]):
            ok = False
        else:
            t[i] = (mid-H[i]) // S[i]
    
    t = sorted(t)
    for i in range(N):
        if t[i] < i:
            ok = False
    if ok:
        right = mid
    else:
        left = mid

print(right)
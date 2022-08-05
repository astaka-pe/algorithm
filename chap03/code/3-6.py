N, W = map(int, input().split())
a = list(map(int, input().split()))

exist = False
for bit in range(1 << N):
    sum = 0
    for i in range(N):
        if bit & (1 << i):
            sum += a[i]
        
    if sum == W:
        exist = True

if exist:
    print("Yes")
else:
    print("No")
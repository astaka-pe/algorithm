N = int(input())
a = list(map(int, input().split()))

max_a = max(a)

left = 0
right = max_a

while(right-left>1):
    counter = 0
    mid = (right+left)//2
    for i in range(N):
        if mid > a[i]:
            counter += 1
    if counter < (N-1)//2:
        left = mid
    else:
        right = mid

ans = max_a
for i in range(N):
    if a[i] >= right:
        if ans > a[i]:
            ans = a[i]
print(ans)
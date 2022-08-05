def func(i, w, a):
    if i == 0:
        if w == 0:
            return True
        else:
            return False
    
    if func(i-1, w, a):
        return True
    if func(i-1, w-a[i-1], a):
        return True
    return False

N, W = map(int, input().split())
a = list(map(int, input().split()))

if func(N, W, a):
    print("Yes")
else:
    print("No")
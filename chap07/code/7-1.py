value = [500, 100, 50, 10, 5, 1]

X = int(input())
a = list(map(int, input().split()))

result = 0
for i in range(len(a)):
    add = X / value[i]
    if add > a[i]:
        add = a[i]
    
    X -= value[i] * add
    result += add

print(result)
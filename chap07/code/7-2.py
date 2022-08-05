N = int(input())
inter = [[] for i in range(N)]
for i in range(N):
    inter[i] = list(map(int, input().split()))

inter = sorted(inter, key=lambda x:x[1])

res = 0
current_end_time = 0

for i in range(N):
    if inter[i][0] < current_end_time:
        continue
    res += 1
    current_end_time = inter[i][1]

print(res)
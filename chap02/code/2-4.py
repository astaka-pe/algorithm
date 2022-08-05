import math

def calc_dist(x1, y1, x2, y2):
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dist

N = int(input())
X = [0]*N
Y = [0]*N

for i in range(N):
    X[i], Y[i] = map(float, input().split())

minimum_dist = math.inf

for i in range(N):
    for j in range(i+1, N):
        dist_i_j = calc_dist(X[i], Y[i], X[j], Y[j])

        if dist_i_j < minimum_dist:
            minimum_dist = dist_i_j

print(minimum_dist)
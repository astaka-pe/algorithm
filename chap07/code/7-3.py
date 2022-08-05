N = int(input())
A = [0]*N
B = [0]*N
for i in range(N):
    A[i], B[i] = map(int, input().split())

sum = 0
for i in range(N-1, -1, -1):
    A[i] += sum
    amari = A[i] % B[i]
    D = 0
    if amari != 0:
        D = B[i] - amari
    sum += D

print(sum)
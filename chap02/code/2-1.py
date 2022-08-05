import time

N = int(input())

start = time.time()

count = 0
for i in range(N):
    count += 1

t = time.time() - start
print("{:4f} seconds".format(t))
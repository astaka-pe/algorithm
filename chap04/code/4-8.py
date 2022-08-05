def fibo(N, memo):
    print("called fibo({})".format(N))
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    if memo[N] != -1:
        return memo[N]
    
    memo[N] = fibo(N-1, memo) + fibo(N-2, memo)
    return memo[N]

N = 6
memo = [-1]*(N+1)
print(fibo(N, memo), memo)

"""
fibo(6) -> fibo(5), fibo(4)
    fibo(5) -> fibo(4), fibo(3)
        fibo(4) -> fibo(3), fibo(2)
            fibo(3) -> fibo(2), fibo(1)
                fibo(2) -> fibo(1), fibo(0)
                    fibo(1)
                    fibo(0)
                fibo(1)
            fibo(2)
        fibo(3)
    fibo(4)
"""
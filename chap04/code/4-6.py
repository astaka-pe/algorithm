def fibo(N):
    print("called fibo({})".format(N))
    if N == 0:
        return 0
    elif N == 1:
        return 1
    result = fibo(N-1) + fibo(N-2)
    print("a[{}]={}".format(N, result))
    return result

print(fibo(6))

"""
fibo(6) -> fibo(5), fibo(4)
    fibo(5) -> fibo(4), fibo(3)
        fibo(4) -> fibo(3), fibo(2)
            fibo(3) -> fibo(2), fibo(1)
                fibo(2) -> fibo(1), fibo(0)
                    fibo(1)
                    fibo(0)
                fibo(1)
            fibo(2) -> fibo(1), fibo(0)
                fibo(1)
                fibo(0)
        fibo(3) -> fibo(2), fibo(1)
            fibo(2) -> fibo(1), fibo(0)
                fibo(1)
                fibo(0)
            fibo(1)
    fibo(4) -> fibo(3), fibo(2)
        fibo(3) -> fibo(2), fibo(1)
                fibo(2) -> fibo(1), fibo(0)
                    fibo(1)
                    fibo(0)
                fibo(1)
            fibo(2) -> fibo(1), fibo(0)
                fibo(1)
                fibo(0)
"""
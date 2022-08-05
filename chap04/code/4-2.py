def func(N):
    print("called func({})".format(N))
    if N == 0:
        return 0
    result = N + func(N-1)
    return result

print(func(5))
def GCD(m, n):
    if n == 0:
        return m
    return GCD(n, m%n)

print(GCD(51, 15))
print(GCD(15, 51))
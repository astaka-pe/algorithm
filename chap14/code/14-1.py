def chmin(a):
    if a[0] > a[1]:
        tmp = a[0]
        a[0] = a[1]
        a[1] = tmp
        return True
    else:
        return False

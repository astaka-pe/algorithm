def root(x):
    if par[x] == -1:
        return x
    else:
        par[x] = root(par[x])
        return par[x]
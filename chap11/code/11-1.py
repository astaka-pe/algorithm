def root(x):
    if par[x] == -1:
        return x
    else:
        return root(par[x])
"""
整数x及び自然数n,mについてx^n(mod m)の計算
"""
def pow_mod(x, n, m):
    if m == 1: return 0  # １で割った余りは常に０
    r = 1
    y = x % m  # mで割ったあまりにする
    while n:
        if n & 1: r = r * y % m  # mで割ったあまりにする
        y = y * y % m  # mで割ったあまりにする
        n >>= 1  
    return r

# 繰り返し二乗法 ＋ modの性質を用いた実装（ACLのpow_modに相当）
print(pow_mod(13, 1000000000, 1000000007))  # 94858115


# Pythonの組み込み関数powを用いた計算
print(pow(13, 1000000000, 1000000007))  # 94858115
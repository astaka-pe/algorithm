"""
整数aと自然数bに対し，
- 最大公約数 gcd(a, b)
- xa = gcd(a,b) (mod b)となるx
を計算
"""

# ユークリッドの互除法
"""
最大公約数を求める問題はより小さな数の最大公約数を求める問題に変えることができる
"""
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

# 拡張ユークリッドの互除法
"""
- ax + by = gcd(a, b)
"""
def inv_gcd(a, b):
    a %= b
    if a == 0: return b, 0
    # 初期状態
    s, t = b, a
    m0, m1 = 0, 1
    while t:
        # 遷移の準備
        u = s // t

        # 遷移
        s -= t * u
        m0 -= m1 * u

        # swap
        s, t = t, s
        m0, m1 = m1, m0

    if m0 < 0: m0 += b // s
    return s, m0

# {g,x,y}: ax + by = g
def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = ext_gcd(b, a%b)
    return g, y, x-a//b*y
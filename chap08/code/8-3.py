# ノードpの直後にノードvを挿入する
def insert(v, p):
    v.next = p.next
    p.next = v
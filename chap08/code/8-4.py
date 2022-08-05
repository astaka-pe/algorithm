class Node:
    def __init__(self, name):
        self.next = None
        self.name = name

START_NODE = Node(None)

# 連結リストを出力する
def print_node():
    cur = START_NODE.next
    while cur != None:
        print(cur.name)
        cur = cur.next

# ノードpの直後にノードvを挿入する
def insert(v, p=START_NODE):
    v.next = p.next
    p.next = v

names = ["yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"]

for i in range(len(names)):
    node = Node(names[i])
    insert(node)
    print("step {}:".format(i))
    print_node()
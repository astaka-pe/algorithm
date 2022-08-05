class Node:
    def __init__(self, name):
        self.prev = None
        self.next = None
        self.name = name

# グローバル変数を使うのは気持ち悪いので、連結リストのクラスを作る

class Linked_list:
    def __init__(self):
        # 先頭ノードの定義
        self.head = Node(None)
        # 末端ノードの定義
        self.last = Node(None)

        self.head.next = self.last
        self.last.prev = self.head
    
    # ノードpの直後にノードvを挿入
    def insert(self, v, p=None):
        if p == None:
            p = self.head
            # ノードpは先頭ノード
            v.next = p.next
            p.next.prev = v
            p.next = v
            v.prev = p
        else:
            v.next = p.next
            p.next.prev = v
            p.next = v
            v.prev = p
    
    # ノードvを削除
    def erase(self, v):
        if v == self.head:
            return
        v.prev.next = v.next
        v.next.prev = v.prev
    
    def print_list(self):
        cur = self.head.next
        while cur != self.last:
            print(cur.name)
            cur = cur.next

names = ["yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"]

linked_list = Linked_list()
erase_node = linked_list.head

for i in range(len(names)):
    node = Node(names[i])
    linked_list.insert(node)

    if names[i] == "ito":
        erase_node = node

print("----------before----------")
linked_list.print_list()
linked_list.erase(erase_node)
print("----------after-----------")
linked_list.print_list()
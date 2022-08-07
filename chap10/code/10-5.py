class Heap:
    def __init__(self):
        self.heap = []
    
    def push(self, x):
        self.heap.append(x)
        i = len(self.heap) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.heap[p] >= x:
                break
            self.heap[i] = self.heap[p]
            i = p
        self.heap[i] = x
    
    def top(self):
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return -1
    
    def pop(self):
        if len(self.heap) == 0:
            return
        x = self.heap[-1]
        self.heap = self.heap[:-1]
        i = 0
        while i*2 + 1 < len(self.heap):
            child1 = i*2 + 1
            child2 = i*2 + 2
            if child2 < len(self.heap):
                if self.heap[child2] > self.heap[child1]:
                    child1 = child2
            if self.heap[child1] <= x:
                break
            self.heap[i] = self.heap[child1]
            i = child1
        self.heap[i] = x

h = Heap()
h.push(5)
h.push(3)
h.push(7)
h.push(1)

print(h.top())
h.pop()
print(h.top())
h.push(11)
print(h.top())
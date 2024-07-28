# next method will be implemented
class Node:
    M = 5

    def __init__(self):
        self.keys = []
        self.values = []
    
    def __repr__(self):
        return str(self.keys)
    
    def is_leaf(self):
        return len(self.keys) == len(self.values)
    
    def bisect(self, key):
        for i, k in enumerate(self.keys):
            if key < k:
                return i
        return len(self.keys)
    
    def insert(self, key, value):
        i = self.bisect(key)
        if self.is_leaf():
            self.values.insert(i, value)
        else:
            self.values.insert(i + 1, value)
        self.keys.insert(i, key)
    
    def split(self):
        m = self.M // 2 + 1
        right = Node()
        if self.is_leaf():
            key = self.keys[m]
            right.keys = self.keys[m:]
            right.values = self.values[m:]
            del self.keys[m:]
            del self.values[m:]
        else:
            key = self.keys[m - 1]
            right.keys = self.keys[m:]
            right.values = self.values[m:]
            del self.keys[m - 1:]
            del self.values[m:]
        return key, right


class BPlusTree:
    def __init__(self):
        self.root = Node()
        self._path = []
    
    def __repr__(self):
        def dfs(node, depth=0):
            print('  ' * depth, node, sep='')
            if node.is_leaf():
                return
            any(dfs(node, depth+1) for node in node.values)
        return str(dfs(self.root))
    
    def search(self, key):
        node = self.root
        self.path = [node]
        while not node.is_leaf():
            i = node.bisect(key)
            node = node.values[i]
            self.path.append(node)
        return node.values[node.keys.index(key)] if key in node.keys else None

    def insert(self, key, value):
        self.search(key)
        while self.path:
            node = self.path.pop()
            node.insert(key, value)
            if len(node.values) <= Node.M:
                return
            key, value = node.split()        
        self.root = Node()
        self.root.keys = [key]
        self.root.values = [node, value]

    def delete(self, key):
        if self.search(key) is None:
            return
        



from random import shuffle, choices

N = 30
A = list(range(N))
A = choices(A, k=len(A))

tree = BPlusTree()
for i in A:
    tree.insert(i, i)

print(tree)

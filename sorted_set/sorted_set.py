class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.size = 1
 
 
class SortedSet(object):
    def __init__(self, A=[]):
        node = None
        for a in sorted(set(A)):
            parent = Node(a)
            parent.left = node
            node = parent
            self._update(node)
        self._root = node
 
    def __bool__(self):
        return bool(self._root)
    
    def __len__(self):
        return self._root.size if self else 0
       
    def __str__(self):
        def dfs(node, res=[]):
            if node is None:
                return []
            dfs(node.left, res)
            res.append(node.value)
            dfs(node.right, res)
            return res
        return str(dfs(self._root))
    
    def _update(self, node):
        node.size = 1
        node.size += node.left.size if node.left else 0
        node.size += node.right.size if node.right else 0
    
    def _rotate(self, v, p, d):
        if d == 0:
            p.left = v.right
            v.right = p
        elif d == 1:
            p.right = v.left
            v.left = p
        self._update(p)
 
    def _splay(self, v, path, direction):
        while len(path) >= 2:
            p, g = path.pop(), path.pop()
            dp, dg = direction.pop(), direction.pop()
            if dp == dg:
                self._rotate(p, g, dg)
                self._rotate(v, p, dp)
            else:
                self._rotate(v, p, dp)
                self._rotate(v, g, dg)
        if path:
            p = path.pop()
            d = direction.pop()
            self._rotate(v, p, d)
        self._update(v)
        self._root = v
    
    def __getitem__(self, i):
        if i < 0:
            i += len(self)
        assert 0 <= i < len(self)
        path, direction = [], []
        v = self._root
        while True:
            lsize = v.left.size if v.left else 0
            if i == lsize:
                break
            path.append(v)
            if i < lsize:
                v = v.left
                direction.append(0)
            else:
                i -= lsize + 1
                v = v.right
                direction.append(1)
        self._splay(v, path, direction)
        return self._root.value
    
    def _merge(self, node):
        if not self:
            self._root = node
        else:
            self[-1]
            self._root.right = node
            self._update(self._root)
    
    def pop(self, i=-1):
        res = self[i]
        self._root, right = self._root.left, self._root.right
        self._merge(right)
        return res
    
    def find(self, value):
        if not self:
            return False
        node = self._root
        path, direction = [], []
        while node and node.value != value:
            path.append(node)
            if node.value > value:
                node = node.left
                direction.append(0)
            else:
                node = node.right
                direction.append(1)
        res = node is not None
        if not res:
            node = path.pop()
            direction.pop()
        self._splay(node, path, direction)
        return res
    
    def add(self, value):
        if self.find(value):
            return False
        node = Node(value)
        if self and self._root.value < value:
            self._root.right, right = None, self._root.right
            self._update(self._root)
            node.left, node.right = self._root, right
        elif self and self._root.value > value:
            left, self._root.left = self._root.left, None
            self._update(self._root)
            node.left, node.right = left, self._root
        self._root = node
        self._update(self._root)
        return True
    
    def erase(self, value):
        if not self.find(value):
            return False
        self.pop(self._root.left.size if self._root.left else 0)
        return True

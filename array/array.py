# https://algorithmtutor.com/Data-Structures/Tree/Splay-Trees/
# https://tjkendev.github.io/procon-library/python/binary_search_tree/splay-tree.html
class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.size = 1
        self.data = None


class Array(object):
    def __init__(self, A, f=None):
        self._f = f
        if isinstance(A, Node) or A is None:
            self._root = A
        else:
            node = None
            for a in A:
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
        if self._f:
            self._f(node)
    
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
    
    def __setitem__(self, i, v):
        self[i]
        self._root.value = v
        self._update(self._root)
    
    def merge(self, other):
        if not self:
            self._root = other._root
        else:
            self[-1]
            self._root.right = other._root
            self._update(self._root)
    
    def split(self, i):
        assert 0 <= i <= len(self)
        if i == len(self):
            return Array(self._root, self._f), Array(None, self._f)
        self[i]
        left, self._root.left = self._root.left, None
        self._update(self._root)
        return Array(left, self._f), Array(self._root, self._f)
    
    def insert(self, i, v):
        left, right = self.split(i)
        self._root = Node(v)
        self._root.left = left._root
        self._root.right = right._root
        self._update(self._root)
    
    def pop(self, i=-1):
        res = self[i]
        self._root, right = self._root.left, self._root.right
        self._update(self._root)
        self.merge(Array(right, self._f))
        return res
    
    def get_data(self):
        return self._root.data

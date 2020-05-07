# Union Find (amortized O(ack^-1(N)))
# https://www.slideshare.net/chokudai/union-find-49066733
class UnionFind(object):
    def __init__(self, n, recursion = False):
        self._par = list(range(n))
        self._size = [1] * n
        self._recursion = recursion

    def root(self, k):
        if self._recursion:
            if k == self._par[k]:
                return k
            self._par[k] = self.root(self._par[k])
            return self._par[k]
        else:
            root = k
            while root != self._par[root]: root = self._par[root]
            while k != root: k, self._par[k] = self._par[k], root
            return root

    def unite(self, i, j):
        i, j = self.root(i), self.root(j)
        if i == j: return False
        if self._size[i] < self._size[j]: i, j = j, i
        self._par[j] = i
        self._size[i] += self._size[j]
        return True

    def is_connected(self, i, j):
        return self.root(i) == self.root(j)

    def size(self, k):
        return self._size[self.root(k)]

# example
uf = UnionFind(6)
uf.unite(0,2)
uf.unite(1,3)
uf.unite(1,5)
print(uf.size(3)) # 3

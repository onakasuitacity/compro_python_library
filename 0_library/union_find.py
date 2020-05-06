# Union Find (amortized O(ack^-1(N)))
# https://www.slideshare.net/chokudai/union-find-49066733
class UnionFind(object):
    def __init__(self, n, recursion = False):
        self.par = list(range(n))
        self.size = [1] * n
        self.recursion = recursion

    def root(self, k):
        if self.recursion:
            if k == self.par[k]:
                return k
            self.par[k] = self.root(self.par[k])
            return self.par[k]
        else:
            root = k
            while root != self.par[root]: root = self.par[root]
            while k != root: k, self.par[k] = self.par[k], root
            return root

    def unite(self, i, j):
        i, j = self.root(i), self.root(j)
        if i == j: return False
        if self.size[i] < self.size[j]: i, j = j, i
        self.par[j] = i
        self.size[i] += self.size[j]
        return True

    def is_connected(self, i, j):
        return self.root(i) == self.root(j)

    def size(self, k):
        return self.size[self.root(k)]

# example
uf = UnionFind(6)
uf.unite(0,2)
uf.unite(1,3)
uf.unite(1,5)
print(uf.size(3)) # 3

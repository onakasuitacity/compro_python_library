# LCA with doubling (O(NlogN),O(logN))
# https://tjkendev.github.io/procon-library/python/graph/lca-doubling.html
class LCA(object):
    def __init__(self, E, root = 0):
        self._n = len(E)
        self._logn = (self._n - 1).bit_length()
        self._parent = [None] * self._logn
        self._dfs(E, root)
        self._doubling()

    def _dfs(self, E, root):
        parent = [-1] * self._n
        depth = [0] * self._n
        stack = [(root, -1)]
        while stack:
            v, p = stack.pop()
            for nv in E[v]:
                if nv == p:
                    continue
                parent[nv] = v
                depth[nv] = depth[v] + 1
                stack.append((nv, v))
        self._parent[0] = parent
        self._depth = depth

    def _doubling(self):
        parent = self._parent[0]
        for k in range(1, self._logn):
            next_parent = [-1] * self._n
            for v in range(self._n):
                if parent[v] == -1:
                    continue
                next_parent[v] = parent[parent[v]]
            self._parent[k] = next_parent
            parent = next_parent

    def lca(self, u, v):
        dd = self._depth[v] - self._depth[u]
        if dd < 0:
            u, v = v, u
            dd *= -1
        for k in range(self._logn):
            if (dd >> k) & 1:
                v = self._parent[k][v]
        if u == v:
            return u
        for k in range(self._logn - 1, -1, -1):
            pu, pv = self._parent[k][u], self._parent[k][v]
            if pu != pv:
                u, v = pu, pv
        return self._parent[0][u]

    @property
    def depth(self):
        return self._depth

    @property
    def parent(self):
        return self._parent

# example
N = 6
V = list(range(N))
E = [[1, 2], [0], [0, 3, 4, 5], [2], [3], [4]]

###
#    0
#   / \
#  1   2
#     /|\
#    3 4 5

lca = LCA(E)
lca.lca(3, 4) 

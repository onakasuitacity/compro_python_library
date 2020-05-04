# LCA with doubling (O(NlogN),O(logN))
# https://tjkendev.github.io/procon-library/python/graph/lca-doubling.html
class LCA(object):
    def __init__(self, E, root = 0):
        self.n = len(E)
        self.logn = (self.n - 1).bit_length()
        self.parent = [None] * self.logn
        self.dfs(E, root)
        self.doubling()

    def dfs(self, E, root):
        parent = [-1] * self.n
        depth = [0] * self.n
        stack = [(root, -1)]
        while stack:
            v, p = stack.pop()
            for nv in E[v]:
                if nv == p:
                    continue
                parent[nv] = v
                depth[nv] = depth[v] + 1
                stack.append((nv, v))
        self.parent[0] = parent
        self.depth = depth

    def doubling(self):
        parent = self.parent[0]
        for k in range(1, self.logn):
            next_parent = [-1] * self.n
            for v in range(self.n):
                if parent[parent[v]] == -1:
                    continue
                next_parent[v] = parent[parent[v]]
            self.parent[k] = next_parent
            parent = next_parent

    def lca(self, u, v):
        dd = self.depth[v] - self.depth[u]
        if dd < 0:
            u, v = v, u
            dd *= -1
        for k in range(self.logn):
            if (dd >> k) & 1:
                v = self.parent[k][v]
        if u == v:
            return u
        for k in range(self.logn - 1, -1, -1):
            pu, pv = self.parent[k][u], self.parent[k][v]
            if pu != pv:
                u, v = pu, pv
        return self.parent[0][u]

# example
N=6
V=list(range(N))
E=[{1,2},{0},{0,3,4,5},{2},{3},{4}]

###
#    0
#   / \
#  1   2
#     /|\
#    3 4 5

a=LCA(E,0)
a.get(3,4) 

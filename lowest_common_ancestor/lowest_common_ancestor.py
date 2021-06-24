# https://tjkendev.github.io/procon-library/python/graph/lca-doubling.html
class LCA(object):
    def __init__(self, G, root=0):
        self._n = len(G)
        self.depth = [0] * self._n
        self.parents = []
        self._bfs(G, root)
        self._doubling()

    def _bfs(self, G, root):
        parent = [-1] * (self._n + 1)
        queue = [(root, -1)]
        for v, p in queue:
            for nv in G[v]:
                if nv == p:
                    continue
                self.depth[nv] = self.depth[v] + 1
                parent[nv] = v
                queue.append((nv, v))
        self.parents.append(parent)

    def _doubling(self):
        for _ in range((self._n - 1).bit_length() - 1):
            parent = self.parents[-1]
            self.parents.append([parent[parent[v]] for v in range(self._n + 1)])

    def lca(self, u, v):
        dd = self.depth[v] - self.depth[u]
        if dd < 0:
            u, v = v, u
            dd *= -1
        for k in range(dd.bit_length()):
            if dd >> k & 1:
                v = self.parents[k][v]
        if u == v:
            return u
        for k in range(self.depth[u].bit_length() - 1, -1, -1):
            pu, pv = self.parents[k][u], self.parents[k][v]
            if pu != pv:
                u, v = pu, pv
        return self.parents[0][u]

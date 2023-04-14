# https://judge.yosupo.jp/submission/25696
# https://www.geeksforgeeks.org/introduction-to-heavy-light-decomposition/
class HeavyLightDecomposition(object):
    def __init__(self, G, root=0):
        N = len(G)
        self._par = [-1] * N
        self._size = [1] * N
        self._heavy_child = [-1] * N
        self._head = [0] * N
        self._order = [0] * N
        self._dfs_heavy_child(G, root)
        self._dfs_decomposition(G, root)
    
    def _dfs_heavy_child(self, G, root):
        par, size, heavy_child = self._par, self._size, self._heavy_child
        stack = [~root, root]
        while stack:
            v = stack.pop()
            if v >= 0:
                for nv in G[v]:
                    if nv != par[v]:
                        par[nv] = v
                        stack.append(~nv)
                        stack.append(nv)
            else:
                v = ~v
                if par[v] != -1:
                    size[par[v]] += size[v]
                for nv in G[v]:
                    if nv == par[v]:
                        continue
                    if heavy_child[v] == -1 or size[nv] > size[heavy_child[v]]:
                        heavy_child[v] = nv
    
    def _dfs_decomposition(self, G, root):
        par, size, heavy_child = self._par, self._size, self._heavy_child
        head, order = self._head, self._order
        stack = [root]
        count = 0
        while stack:
            v = stack.pop()
            order[v] = count
            count += 1
            head[v] = head[par[v]] if order[par[v]] == order[v] - 1 else v
            for nv in G[v]:
                if nv != par[v] and nv != heavy_child[v]:
                    stack.append(nv)
            if heavy_child[v] != -1:
                stack.append(heavy_child[v])
    
    def lca(self, u, v):
        par, head, order = self._par, self._head, self._order
        while True:
            if order[u] > order[v]:
                u, v = v, u
            if head[u] == head[v]:
                return u
            v = par[head[v]]

    def _ascend(self, u, v):
        par, head, order = self._par, self._head, self._order
        res = []
        while head[u] != head[v]:
            res.append((order[u], order[head[u]]))
            u = par[head[u]]
        if u != v:
            res.append((order[u], order[v] + 1))
        return res
    
    def _descend(self, u, v):
        return [(j, i) for i, j in self._ascend(v, u)[::-1]]
    
    def path(self, u, v, edge=False):
        l = self.lca(u, v)
        return self._ascend(u, l) + ([] if edge else [(self._order[l], self._order[l])]) + self._descend(l, v)
    
    def get_order(self):
        return self._order
    
    def edge_to_order(self, E):
        par, order = self._par, self._order
        return [order[u] if par[u] == v else order[v] for u, v in E]

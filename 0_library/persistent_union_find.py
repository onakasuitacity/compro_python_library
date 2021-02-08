k = 20
class PersistentArray(object):
    def __init__(self, A):
        if isinstance(A, list):
            queue = [(A[0], [None] * k)]
            for i, node in enumerate(queue):
                for j in range(k):
                    ni = k * i + j + 1
                    if ni < len(A):
                        node[1][j] = (A[ni], [None] * k)
                        queue.append(node[1][j])
            self.root = queue[0]
        else:
            self.root = A

    def __getitem__(self, i):
        node = self.root
        path = []
        while i:
            i, r = divmod(i - 1, k)
            path.append(r)
        for i in path[::-1]:
            node = node[1][i]
        return node[0]

    def set(self, i, v):
        node = self.root
        path = []
        while i:
            i, r = divmod(i - 1, k)
            path.append(r)
        stack = []
        for i in path[::-1]:
            stack.append((node[0], node[1][:]))
            node = node[1][i]
        node = (v, node[1])
        for i in path:
            stack[-1][1][i] = node
            node = stack.pop()
        return PersistentArray(node)

class PersistentUnionFind(object):
    def __init__(self, n):
        if isinstance(n, int):
            self._par = PersistentArray(list(range(n)))
            self._size = PersistentArray([1] * n)
        else:
            self._par, self._size = n

    def root(self, i):
        root, par = i, self._par[i]
        while root != par:
            root, par = par, self._par[par]
        return root

    def unite(self, i, j):
        i, j = self.root(i), self.root(j)
        if i == j:
            return self
        if self.size(i) < self.size(j):
            i, j = j, i
        par = self._par.set(j, i)
        size = self._size.set(i, self.size(i) + self.size(j))
        return PersistentUnionFind((par, size))

    def is_connected(self, i, j):
        return self.root(i) == self.root(j)

    def size(self, i):
        return self._size[self.root(i)]

# segment tree (without lazy-propagation)
class SegmentTree(object):
    def __init__(self, A, dot, e):
        n = len(A)
        tree = [e] * n + A
        for i in range(n - 1, 0, -1):
            tree[i] = dot(tree[i << 1], tree[i << 1 | 1])
        self._n, self._tree, self._dot, self._e = n, tree, dot, e

    def __getitem__(self, i):
        return self._tree[i + self._n]

    def __setitem__(self, i, v):
        i += self._n
        self._tree[i] = v
        while i != 1:
            i >>= 1
            self._tree[i] = self._dot(self._tree[i << 1], self._tree[i << 1 | 1])

    def sum(self, l, r):
        l += self._n
        r += self._n
        lv = rv = self._e
        while l < r:
            if l & 1:
                lv = self._dot(lv, self._tree[l])
                l += 1
            if r & 1:
                r -= 1
                rv = self._dot(self._tree[r], rv)
            l >>= 1
            r >>= 1
        return self._dot(lv, rv)

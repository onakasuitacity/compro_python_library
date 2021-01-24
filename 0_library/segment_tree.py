# segment tree (without lazy-propagation)
class SegmentTree(object):
    def __init__(self, A, dot, unit):
        n = 1 << (len(A) - 1).bit_length()
        tree = [unit] * (2 * n)
        tree[n : n + len(A)] = A
        for i in range(n - 1, 0, -1):
            tree[i] = dot(tree[i << 1], tree[i << 1 | 1])
        self._n, self._tree, self._dot, self._unit = n, tree, dot, unit

    def __getitem__(self, i):
        if isinstance(i, int):
            return self._tree[i + self._n]
        elif isinstance(i, slice):
            s = self._n if i.start is None else i.start + self._n
            t = self._n if i.stop is None else i.stop + self._n
            w = i.step
            return self._tree[s:t:w]
        else:
            raise TypeError("SegmentTree indices must be integers or slices")

    def __setitem__(self, i, v):
        i += self._n
        self._tree[i] = v
        while i != 1:
            i >>= 1
            self._tree[i] = self._dot(self._tree[i << 1], self._tree[i << 1 | 1])

    def sum(self, l, r):
        l += self._n
        r += self._n
        lv = rv = self._unit
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

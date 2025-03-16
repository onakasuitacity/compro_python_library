# lazy-propagation segment tree
# http://tsutaj.hatenablog.com/entry/2017/03/30/224339
# http://beet-aizu.hatenablog.com/entry/2017/12/01/225955
# http://sugarknri.hatenablog.com/entry/2018/04/16/123016
class LazySegmentTree(object):
    def __init__(self, A, dot, e, compose, id, act):
        n = len(A)
        tree = [e] * n + A
        for i in range(n - 1, 0, -1):
            tree[i] = dot(tree[i << 1], tree[i << 1 | 1])
        self._n, self._tree, self._lazy = n, tree, [id] * 2 * n
        self._dot, self._e, self._compose, self._id, self._act = dot, e, compose, id, act

    def _ascend(self, i):
        tree, lazy, dot, act = self._tree, self._lazy, self._dot, self._act
        while i > 1:
            i >>= 1
            tree[i] = act(lazy[i], dot(tree[i << 1], tree[i << 1 | 1]))

    def _descend(self, i):
        tree, lazy, id, compose, act = self._tree, self._lazy, self._id, self._compose, self._act
        for k in range(i.bit_length() - 1, 0, -1):
            p = i >> k
            f = lazy[p]
            tree[p << 1], lazy[p << 1] = act(f, tree[p << 1]), compose(f, lazy[p << 1])
            tree[p << 1 | 1], lazy[p << 1 | 1] = act(f, tree[p << 1 | 1]), compose(f, lazy[p << 1 | 1])
            lazy[p] = id

    def act(self, l, r, f):
        l += self._n
        r += self._n
        # self._descend(l), self._descend(r - 1)  # unnecessary when compose is commutative
        _l, _r = l, r
        tree, lazy, act, compose = self._tree, self._lazy, self._act, self._compose
        while l < r:
            if l & 1:
                tree[l], lazy[l] = act(f, tree[l]), compose(f, lazy[l])
                l += 1
            if r & 1:
                r -= 1
                tree[r], lazy[r] = act(f, tree[r]), compose(f, lazy[r])
            l >>= 1
            r >>= 1
        self._ascend(_l), self._ascend(_r - 1)

    def sum(self, l, r):
        l += self._n
        r += self._n
        self._descend(l), self._descend(r - 1)
        lv = rv = self._e
        tree, dot = self._tree, self._dot
        while l < r:
            if l & 1:
                lv = dot(lv, tree[l])
                l += 1
            if r & 1:
                r -= 1
                rv = dot(tree[r], rv)
            l >>= 1
            r >>= 1
        return dot(lv, rv)

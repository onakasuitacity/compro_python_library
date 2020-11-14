# https://smijake3.hatenablog.com/entry/2018/06/16/144548
class LiChaoTree(object):
    def __init__(self, X):
        X = sorted(set(X))
        N = 1 << (len(X) - 1).bit_length()
        self._tree = [None] * (N << 1)
        self._N, self._X = N, X + [INF] * (N - len(X))
        self._X_inv = {x : i for i, x in enumerate(X)}

    def add_line(self, a, b, i = 1):
        N, tree, X = self._N, self._tree, self._X
        k = i.bit_length() - 1
        l, r = (i - (1 << k)) * (N >> k), (i - (1 << k) + 1) * (N >> k)
        while l < r:
            if tree[i] is None:
                tree[i] = (a, b)
                return
            m = (l + r) >> 1
            ai, bi = tree[i]
            left = a * X[l] + b < ai * X[l] + bi
            mid = a * X[m] + b < ai * X[m] + bi
            right = a * X[r-1] + b < ai * X[r-1] + bi
            if left is right:
                if left:
                    tree[i] = (a, b)
                return
            if mid:
                tree[i], a, b = (a, b), ai, bi
            if left is not mid:
                i, r = i << 1, m
            else:
                i, l = i << 1 | 1, m

    def add_segment(self, l, r, a, b):
        l, r = self._X_inv[l] + self._N, self._X_inv[r] + self._N
        while l < r:
            if l & 1:
                self.add_line(a, b, l)
                l += 1
            if r & 1:
                r -= 1
                self.add_line(a, b, r)
            l >>= 1
            r >>= 1

    def get_min(self, x):
        i = self._X_inv[x] + self._N
        tree = self._tree
        res = INF
        while i:
            if tree[i] is not None:
                a, b = tree[i]
                res = min(res, a * x + b)
            i >>= 1
        return res

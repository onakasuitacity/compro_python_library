# https://ei1333.github.io/luzhiled/snippets/string/rolling-hash.html
# http://perogram.hateblo.jp/entry/rolling_hash
from random import randrange
class RollingHash(object):
    _b, _p = randrange(140, 999), (1 << 61) - 1

    @classmethod
    def add(cls, hash1, hash2):
        h1, l1 = hash1
        h2, l2 = hash2
        return (h1 * l2 + h2) % cls._p, l1 * l2 % cls._p

    def __init__(self, S):
        n = len(S)
        b, add = self._b, self.add
        tree = [(0, 1)] * n + [(ord(c), b) for c in S]
        for i in range(n - 1, 0, -1):
            tree[i] = add(tree[i << 1], tree[i << 1 | 1])
        self._n, self._tree = n, tree
    
    def __getitem__(self, x):
        l, r = x.start, x.stop
        l += self._n
        r += self._n
        tree, add = self._tree, self.add
        lv = rv = (0, 1)
        while l < r:
            if l & 1:
                lv = add(lv, tree[l])
                l += 1
            if r & 1:
                r -= 1
                rv = add(tree[r], rv)
            l >>= 1
            r >>= 1
        return add(lv, rv)

    def __setitem__(self, i, c):
        i += self._n
        tree, add = self._tree, self.add
        tree[i] = (ord(c), self._b)
        while i != 1:
            i >>= 1
            tree[i] = add(tree[i << 1], tree[i << 1 | 1])

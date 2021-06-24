# https://ei1333.github.io/luzhiled/snippets/string/rolling-hash.html
# http://perogram.hateblo.jp/entry/rolling_hash
class RollingHash(object):
    _b, _p = 1007, (1 << 61) - 1
    N = 100000
    power = [1] * (N + 1)
    for i in range(N):
        power[i + 1] = power[i] * _b % _p

    def __init__(self, S):
        self._n = n = len(S)
        b, p = self._b, self._p
        hash = [0] * (n + 1)
        for i, s in enumerate(S):
            hash[i + 1] = hash[i] * b % p + ord(s)
        self._hash = hash

    def __getitem__(self, x):
        l, r = x.start, x.stop
        return (self._hash[r] - self._hash[l] * self.power[r - l]) % self._p, r - l

    @classmethod
    def add(cls, hash1, hash2):
        h1, l1 = hash1
        h2, l2 = hash2
        return (h1 * cls.power[l2] + h2) % cls._p, l1 + l2

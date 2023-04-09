# https://scrapbox.io/data-structures/Wavelet_Matrix
# https://echizen-tm.hatenadiary.org/entry/20120801/1343837130
class BitVector(object):
    def __init__(self, A):
        S = [0] * (len(A) + 1)
        for i, a in enumerate(A):
            S[i + 1] = S[i] + a
        self._S = S
    
    def __len__(self):
        return len(self._S) - 1
    
    def __getitem__(self, i):
        return self._S[i + 1] - self._S[i]
    
    def rank(self, v, i):
        return (1 - v) * i + (2 * v - 1) * self._S[i]
    
    def select(self, v, i):
        assert 0 <= i < self.rank(v, len(self))
        l, r = 0, len(self)
        while r - l > 1:
            m = l + r >> 1
            if self.rank(v, m) > i:
                r = m
            else:
                l = m
        return l


class WaveletMatrix(object):
    def __init__(self, A):
        log = max(1, max(a.bit_length() for a in A))
        data = [None] * log
        mid = [0] * log
        for d in range(log - 1, -1, -1):
            V, L, R = [], [], []
            for a in A:
                if a >> d & 1:
                    V.append(1)
                    R.append(a)
                else:
                    V.append(0)
                    L.append(a)
            data[d] = BitVector(V)
            mid[d] = len(L)
            A = L + R
        self._log, self._data, self._mid = log, data, mid
    
    def __len__(self):
        return len(self._data[0])

    def __getitem__(self, i):
        res = 0
        data, mid = self._data, self._mid
        for d in range(self._log - 1, -1, -1):
            if data[d][i]:
                res |= 1 << d
                i = data[d].rank(1, i) + mid[d]
            else:
                i = data[d].rank(0, i)
        return res

    def rank(self, v, i):
        l, r = 0, i
        data, mid = self._data, self._mid
        for d in range(self._log - 1, -1, -1):
            if v >> d & 1:
                l = data[d].rank(1, l) + mid[d]
                r = data[d].rank(1, r) + mid[d]
            else:
                l = data[d].rank(0, l)
                r = data[d].rank(0, r)
        return r - l

    def select(self, v, i):
        res = 0
        data, mid = self._data, self._mid
        for d in range(self._log - 1, -1, -1):
            if v >> d & 1:
                res = data[d].rank(1, res) + mid[d]
            else:
                res = data[d].rank(0, res)
        res += i
        for d in range(self._log):
            if v >> d & 1:
                res = data[d].select(1, res - mid[d])
            else:
                res = data[d].select(0, res)
        return res

    def quantile(self, l, r, k):
        res = 0
        data, mid = self._data, self._mid
        for d in range(self._log - 1, -1, -1):
            cnt = data[d].rank(0, r) - data[d].rank(0, l)
            if cnt <= k:
                res |= 1 << d
                k -= cnt
                l = data[d].rank(1, l) + mid[d]
                r = data[d].rank(1, r) + mid[d]
            else:
                l = data[d].rank(0, l)
                r = data[d].rank(0, r)
        return res

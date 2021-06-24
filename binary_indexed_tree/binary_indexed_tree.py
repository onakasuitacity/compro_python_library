class BIT(object):
    def __init__(self, arr):
        self.n = n = len(arr)
        self.bit = bit = [0] * (n + 1)
        for i, a in enumerate(arr, 1):
            bit[i] += a
            ni = i + (i & -i)
            if ni <= n:
                bit[ni] += bit[i]

    def add(self, i, v):
        # assert 0 <= i < self.n
        i += 1
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def sum(self, i):
        # assert 0 <= i <= self.n
        s = 0
        while i:
            s += self.bit[i]
            i -= i & -i
        return s

    def find(self, k):
        # assert k >= 0
        di = 1 << (self.n - 1).bit_length()
        i = s = 0
        while di:
            ni = i + di
            if ni <= self.n:
                ns = s + self.bit[ni]
                if ns < k:
                    i, s = ni, ns
            di >>= 1
        return i if i < self.n else -1

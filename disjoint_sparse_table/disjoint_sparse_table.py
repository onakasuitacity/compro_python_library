# https://ei1333.github.io/library/structure/others/disjoint-sparse-table.hpp
class DisjointSparseTable(object):
    def __init__(self, A, dot):
        N = len(A)
        logN = (N - 1).bit_length()
        data = [A[:]]
        for i in range(1, logN):
            shift = 1 << i
            nA = A[:]
            for l in range(0, N, shift << 1):
                m, r = min(l + shift, N), min(l + (shift << 1), N)
                for j in range(m - 2, l - 1, -1):
                    nA[j] = dot(nA[j], nA[j + 1])
                for j in range(m + 1, r):
                    nA[j] = dot(nA[j - 1], nA[j])
            data.append(nA)
        self._data, self._dot = data, dot
    
    def sum(self, l, r):
        r -= 1
        if l == r:
            return self._data[0][l]
        msb = (l ^ r).bit_length() - 1
        return self._dot(self._data[msb][l], self._data[msb][r])

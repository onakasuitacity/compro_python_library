# https://mametter.hatenablog.com/entry/20180130/p1
# http://web.stanford.edu/class/archive/cs/cs166/cs166.1196/lectures/04/Slides04.pdf
# https://niuez.hatenablog.com/entry/2019/12/16/203739
# https://judge.yosupo.jp/submission/1069
class SuffixArray(object):
    def __init__(self, S):
        self.S = S
        self.sa = self._sa_is(list(map(ord, S + '$')))
        self.lcp = self._lcp_array(S + '$', self.sa)
        self.table = self._sparce_table(self.lcp)

    def _sa_is(self, S):
        n = len(S)
        stype = [True] * n
        for i in range(n - 2, -1, -1):
            if S[i] == S[i + 1]:
                stype[i] = stype[i + 1]
            else:
                stype[i] = S[i] < S[i + 1]

        lms = []
        lms_map = [-1] * n
        for i in range(1, n):
            if not stype[i - 1] and stype[i]:
                lms_map[i] = len(lms)
                lms.append(i)

        k = max(S) + 1
        bucket = [0] * k
        for v in S:
            bucket[v] += 1
        cum = [0] * (k + 1)
        for i in range(k):
            cum[i + 1] = cum[i] + bucket[i]

        def induced_sort():
            buf = cum[:]
            for i in lms[::-1]:
                v = S[i]
                buf[v + 1] -= 1
                sa[buf[v + 1]] = i
            buf = cum[:]
            for i in range(n):
                if sa[i] != -1 and not stype[sa[i] - 1]:
                    v = S[sa[i] - 1]
                    sa[buf[v]] = sa[i] - 1
                    buf[v] += 1
            buf = cum[:]
            for i in range(n - 1, -1, -1):
                if stype[sa[i] - 1]:
                    v = S[sa[i] - 1]
                    buf[v + 1] -= 1
                    sa[buf[v + 1]] = sa[i] - 1

        sa = [-1] * n
        induced_sort()

        if len(lms) <= 2:
            return sa

        _lms = lms
        lms = [s for s in sa if lms_map[s] != -1]
        lms_substr = list(range(len(lms)))
        for i in range(2, len(lms)):
            l, r = lms[i - 1], lms[i]
            if S[l] != S[r]:
                lms_substr[i] = lms_substr[i - 1] + 1
                continue
            while True:
                l += 1
                r += 1
                if S[l] != S[r] or lms_map[l] * lms_map[r] < 0:
                    lms_substr[i] = lms_substr[i - 1] + 1
                    break
                if lms_map[l] >= 0 and lms_map[r] >= 0:
                    lms_substr[i] = lms_substr[i - 1]
                    break

        sub_s = [0] * len(lms)
        for i, v in zip(lms, lms_substr):
            sub_s[lms_map[i]] = v
        lms = [_lms[s] for s in self._sa_is(sub_s)]

        sa = [-1] * n
        induced_sort()
        return sa

    def _lcp_array(self, S, sa):
        n = len(S)
        rank = [0] * n
        for i in range(n):
            rank[sa[i]] = i
        lcp = [0] * (n - 1)
        h = 0
        for i in range(n - 1):
            j = sa[rank[i] - 1]
            if h:
                h -= 1
            while j + h < n and i + h < n and S[j + h] == S[i + h]:
                h += 1
            lcp[rank[i] - 1] = h
        self._rank = rank
        return lcp

    def _sparce_table(self, A):
        n = len(A)
        logn = max(1, (n - 1).bit_length())
        table = [[0] * n for _ in range(logn)]
        table[0] = A[:]
        for i in range(1, logn):
            for k in range(n):
                if k + (1 << (i - 1)) >= n:
                    table[i][k] = table[i - 1][k]
                else:
                    table[i][k] = min(table[i - 1][k], table[i - 1][k + (1 << (i - 1))])
        return table

    def get_lcp(self, i, j):
        l, r = self._rank[i], self._rank[j]
        l, r = min(l, r), max(l, r)
        d = max(0, (r - l - 1).bit_length() - 1)
        return min(self.table[d][l], self.table[d][r - (1 << d)])

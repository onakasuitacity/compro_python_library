# https://people.orie.cornell.edu/dpw/orie633/
# https://misawa.github.io/others/flow/lets_use_capacity_scaling.html
from heapq import heappop, heappush
class MinCostFlow(object):
    def __init__(self, n):
        self.n = n
        self.E = [[] for _ in range(n + 1)]
        self.edges = []
        self._b = [0] * (n + 1)
        self._u = 1

    def add_supply(self, v, b):
        self.add_edge(self.n, v, b, b, 0, False)

    def add_edge(self, u, v, lower, upper, cost, append = True):
        e = [v, upper, cost, 0]
        rev = [u, -lower, -cost, e]
        e[-1] = rev
        self.E[u].append(e)
        self.E[v].append(rev)
        self._u = max(self._u, upper - lower)
        if not lower <= 0 <= upper:
            self._push(e, lower)
        if append:
            self.edges.append((e, upper))

    def _push(self, e, f):
        rev = e[-1]
        self._b[rev[0]] -= f
        self._b[e[0]] += f
        e[1] -= f
        rev[1] += f

    def _saturate(self, delta):
        for v in range(self.n + 1):
            for e in self.E[v]:
                nv, cap, cost, _ = e
                if cap >= delta and cost + self.p[v] - self.p[nv] < 0:
                    self._push(e, cap)

    def _shortest_path(self, delta):
        n = self.n + 1
        dist = [INF] * n
        heap = []
        for v, b in enumerate(self._b):
            if b >= delta:
                dist[v] = 0
                heap.append((0, v))
        prev = [None] * n
        while heap:
            d, v = heappop(heap)
            if dist[v] != d:
                continue
            if self._b[v] <= -delta:
                while prev[v]:
                    e = prev[v]
                    self._push(e, delta)
                    v = e[-1][0]
                for v in range(n):
                    self.p[v] += min(d, dist[v])
                return True
            for e in self.E[v]:
                nv, cap, cost, _ = e
                if cap < delta:
                    continue
                if dist[nv] > d + cost + self.p[v] - self.p[nv]:
                    prev[nv] = e
                    dist[nv] = d + cost + self.p[v] - self.p[nv]
                    heappush(heap, (dist[nv], nv))
        return False

    def solve(self):
        self.p = [0] * (self.n + 1)
        delta = 1 << (self._u - 1).bit_length()
        while delta:
            self._saturate(delta)
            while self._shortest_path(delta):
                pass
            delta >>= 1
        self.p.pop()
        return all(b == 0 for b in self._b)

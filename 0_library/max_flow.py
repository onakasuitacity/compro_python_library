# https://people.orie.cornell.edu/dpw/orie633/
# https://ta1sa.hatenablog.com/entry/2020/04/13/123802
# https://www.youtube.com/watch?v=_SdF4KK_dyM
# https://atcoder.jp/contests/practice2/submissions/16784996
class MaxFlow(object):
    def __init__(self, n):
        self.n = n
        self.E = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        e = [v, cap, 0]
        rev = [u, 0, e]
        e[2] = rev
        self.E[u].append(e)
        self.E[v].append(rev)

    def _bfs(self, s, t):
        self._level = level = [-1] * self.n
        level[s] = 0
        queue = [s]
        for v in queue:
            for nv, cap, _ in self.E[v]:
                if cap and level[nv] == -1:
                    level[nv] = level[v] + 1
                    if nv == t:
                        return True
                    queue.append(nv)
        return level[t] != -1

    def _dfs(self, s, t):
        E, level, it = self.E, self._level, self._iter
        stack = [(s, INF)]
        while stack:
            v, f = stack[-1]
            if v == t:
                for v, _ in stack[:-1]:
                    E[v][it[v]][1] -= f
                    E[v][it[v]][2][1] += f
                return f
            while it[v] < len(E[v]):
                nv, cap, _ = E[v][it[v]]
                if cap and level[v] < level[nv]:
                    stack.append((nv, min(f, cap)))
                    break
                it[v] += 1
            else:
                stack.pop()
                level[v] = 0
        return 0

    def solve(self, s, t):
        res = 0
        while self._bfs(s, t):
            self._iter = [0] * self.n
            f = 1
            while f:
                f = self._dfs(s, t)
                res += f
        return res

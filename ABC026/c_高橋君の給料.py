# https://atcoder.jp/contests/abc026/tasks/abc026_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    E=[[] for _ in range(n)]
    for v in range(1,n):
        u=int(input())-1
        E[u].append(v)

    dp=[None]*n
    def dfs(v)->int:
        if(dp[v] is not None): return dp[v]
        if(not E[v]):
            dp[v]=1
            return dp[v]
        M=max(dfs(nv) for nv in E[v])
        m=min(dfs(nv) for nv in E[v])
        dp[v]=M+m+1
        return dp[v]

    print(dfs(0))
resolve()

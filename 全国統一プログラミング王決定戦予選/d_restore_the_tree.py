# https://atcoder.jp/contests/nikkei2019-qual/tasks/nikkei2019_qual_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    E=[[] for _ in range(n)]
    R=[[] for _ in range(n)]
    for _ in range(n-1+m):
        u,v=map(int,input().split())
        u-=1; v-=1
        E[u].append(v)
        R[v].append(u)

    # longest path (topological sort)
    dp=[None]*n
    def dfs(v):
        if(dp[v] is not None):
            return dp[v]
        res=0
        for nv in E[v]:
            res=max(res,dfs(nv)+1)
        dp[v]=res
        return res

    for v in range(n):
        dfs(v)

    # 各頂点に対して、逆辺の dp の値の最小が親
    ans=[None]*n
    root=max((dp[v],v) for v in range(n))[1]
    ans[root]=-1
    for v in range(n):
        if(v==root): continue
        p=min((dp[p],p) for p in R[v])[1]
        ans[v]=p

    print(*map(lambda x:x+1,ans),sep='\n')
resolve()

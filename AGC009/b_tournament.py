# https://atcoder.jp/contests/agc009/tasks/agc009_b
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
        E[v].append(u)

    dp=[None]*n
    def dfs(v,p=-1)->int:
        if(dp[v] is not None): return dp[v]
        if(E[v]==[p]): # 葉のとき 0
            dp[v]=0
            return 0
        res=[]
        for nv in E[v]:
            if(nv==p): continue
            res.append(dfs(nv,v))
        dp[v]=max(1+i+x for i,x in enumerate(sorted(res,reverse=1)))
        return dp[v]

    print(dfs(0))
resolve()

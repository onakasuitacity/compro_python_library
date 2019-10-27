# https://atcoder.jp/contests/abc144/tasks/abc144_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(m):
        s,t=map(int,input().split())
        s-=1; t-=1
        E[s].append(t)
    dp=[0]*n
    for v in range(n-2,-1,-1):
        for nv in E[v]:
            dp[v]+=dp[nv]
        dp[v]/=len(E[v])
        dp[v]+=1
    ans=dp[0]

    # u→nu を削除する
    for u in range(n):
        if(len(E[u])<=1): continue
        nu=max(*((dp[nu],nu) for nu in E[u]))[1]
        dp2=[0]*n
        for v in range(n-2,-1,-1):
            for nv in E[v]:
                if(v==u and nv==nu): continue
                dp2[v]+=dp2[nv]
            dp2[v]/=(len(E[v]) if v!=u else len(E[v])-1)
            dp2[v]+=1
        ans=min(ans,dp2[0])
    print(ans)
resolve()

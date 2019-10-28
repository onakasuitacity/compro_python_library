# https://atcoder.jp/contests/abc144/tasks/abc144_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    edges=[[] for _ in range(n)]
    for _ in range(m):
        s,t=map(int,input().split())
        s-=1; t-=1
        edges[s].append(t)

    # 確率DP
    p=[0]*n
    p[0]=1.0
    for v in range(n):
        for nv in edges[v]:
            p[nv]+=p[v]/len(edges[v])

    # 期待値DP
    E=[0]*n
    for v in range(n-2,-1,-1):
        for nv in edges[v]:
            E[v]+=E[nv]
        E[v]=1+E[v]/len(edges[v])

    ans=E[0]
    for v in range(n):
        if(len(edges[v])<=1): continue
        # 各vに対して、辺vwのうちE[w]が最大のものを削除する
        w=max(*((E[w],w) for w in edges[v]))[1]
        E_dash=0
        for nv in edges[v]:
            if(nv==w): continue
            E_dash+=E[nv]
        E_dash=1+E_dash/(len(edges[v])-1)
        dE=E_dash-E[v]
        ans=min(ans,E[0]+p[v]*dE)

    print(ans)
resolve()

# https://atcoder.jp/contests/abc138/tasks/abc138_d
# PyPyではTLE,Pythonで1719ms
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,q=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=map(int,input().split())
        a-=1; b-=1
        E[a].append(b)
        E[b].append(a)
    ans=[0]*n
    for _ in range(q):
        p,x=map(int,input().split())
        p-=1
        ans[p]+=x

    def dfs(v,p=-1):
        for u in E[v]:
            if u==p: continue
            ans[u]+=ans[v]
            dfs(u,v)

    dfs(0)
    print(*ans)

resolve()

# https://atcoder.jp/contests/abc126/tasks/abc126_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    E=[[] for _ in range(n)]
    for _ in range(n-1):
        u,v,w=map(int,input().split())
        u-=1; v-=1; w%=2
        E[u].append((v,w))
        E[v].append((u,w))

    d=[0]*n
    def dfs(v,p):
        for nv,w in E[v]:
            if(nv==p): continue
            d[nv]=d[v]^w
            dfs(nv,v)
    dfs(0,-1)
    print(*d,sep='\n')
resolve()

# https://atcoder.jp/contests/abc061/tasks/abc061_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n,m=map(int,input().split())
    dist=[float("inf")]*n
    dist[0]=0
    edges=[0]*m
    for i in range(m):
        a,b,c=map(int,input().split())
        edges[i]=[a-1,b-1,-c]

    # Bellman-Ford
    for k in range(1,2*n): # 2n-1回やって、n-1と2n-1のscoreを見る
        for u,v,cost in edges:
            if dist[v]>dist[u]+cost:
                dist[v]=dist[u]+cost
        if k==n-1:
            ans=dist[n-1]

    print(-ans if ans==dist[n-1] else "inf")

resolve()

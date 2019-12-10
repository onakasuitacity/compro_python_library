# https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from heapq import heappop,heappush
def resolve():
    n,m,s,t=map(int,input().split())
    s-=1; t-=1
    E=[[] for _ in range(n)]
    R=[[] for _ in range(n)]
    for _ in range(m):
        u,v,a,b=map(int,input().split())
        u-=1; v-=1
        E[u].append((v,a))
        E[v].append((u,a))
        R[u].append((v,b))
        R[v].append((u,b))

    # Dijkstra with heapq
    dist1=[INF]*n
    dist1[s]=0
    Q=[(0,s)]
    while(Q):
        d,v=heappop(Q)
        if(dist1[v]<d): continue
        for nv,w in E[v]:
            if(dist1[nv]>dist1[v]+w):
                dist1[nv]=dist1[v]+w
                heappush(Q,(dist1[nv],nv))

    dist2=[INF]*n
    dist2[t]=0
    Q=[(0,t)]
    while(Q):
        d,v=heappop(Q)
        if(dist2[v]<d): continue
        for nv,w in R[v]:
            if(dist2[nv]>dist2[v]+w):
                dist2[nv]=dist2[v]+w
                heappush(Q,(dist2[nv],nv))

    # s -> v -> t の最短を計測する
    dist=[dist1[v]+dist2[v] for v in range(n)]
    # 後ろから min をとる
    for i in range(n-1,0,-1):
        dist[i-1]=min(dist[i-1],dist[i])

    M=10**15
    for v in range(n):
        print(M-dist[v])
resolve()

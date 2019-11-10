# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    E=[[] for _ in range(n)]
    for i in range(1,n):
        E[i].append((i-1,0))
    for _ in range(m):
        l,r,c=map(int,input().split())
        l-=1; r-=1
        E[l].append((r,c))

    # Dijkstra with heap
    from heapq import heappop,heappush
    Q=[(0,0)]
    dist=[INF]*n
    dist[0]=0
    while(Q):
        d,v=heappop(Q)
        if(dist[v]<d): continue
        for nv,w in E[v]:
            if(dist[nv]>dist[v]+w):
                dist[nv]=dist[v]+w
                heappush(Q,(dist[nv],nv))
    ans=dist[-1]
    if(ans==INF): ans=-1
    print(ans)
resolve()

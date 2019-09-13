# https://atcoder.jp/contests/abc035/submissions/7493216
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n,m,t=map(int,input().split())
    A=list(map(int,input().split()))
    V=list(range(n))
    E=[[] for _ in range(n)]
    revE=[[] for _ in range(n)]

    # input
    for _ in range(m):
        a,b,c=map(int,input().split())
        a-=1
        b-=1
        E[a].append([b,c])
        revE[b].append([a,c])

    # Dijkstra
    d=[INF]*n
    d[0]=0
    revd=[INF]*n
    revd[0]=0

    # iterate
    import heapq
    Q=[]
    heapq.heapify(Q)
    heapq.heappush(Q,(0,0)) # (cost,v)
    while(Q):
        dist,v=heapq.heappop(Q)
        if d[v]<dist: continue # 候補として挙がったdist,vだが、他で短いのがある
        for i,cost in E[v]:
            if d[i]>d[v]+cost:
                d[i]=d[v]+cost
                heapq.heappush(Q,(d[i],i))

    Q=[]
    heapq.heapify(Q)
    heapq.heappush(Q,(0,0)) # (cost,v)
    while(Q):
        dist,v=heapq.heappop(Q)
        if revd[v]<dist: continue # 候補として挙がったdist,vだが、他で短いのがある
        for i,cost in revE[v]:
            if revd[i]>revd[v]+cost:
                revd[i]=revd[v]+cost
                heapq.heappush(Q,(revd[i],i))

    print(max(A[i]*(t-d[i]-revd[i]) for i in range(n)))

resolve()

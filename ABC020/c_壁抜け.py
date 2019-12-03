# https://atcoder.jp/contests/abc020/tasks/abc020_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

def bisection(l,r,f,left=True,discrete=True):
    eps=1 if discrete else 10**-12
    if((not left)^f(r)): return r if left else r+1
    elif(left^f(l)): return l-1 if left else l
    while(r-l>eps):
        h=(l+r)//2 if discrete else (l+r)/2
        if((not left)^f(h)): l=h
        else: r=h
    return (l+r)/2 if not discrete else l if left else r

def resolve():
    h,w,t=map(int,input().split())
    n=h*w
    # grid を 1-dim で持つ
    G=[s for _ in range(h) for s in input()]
    s=G.index('S')
    g=G.index('G')
    D=[(-1,0),(1,0),(0,-1),(0,1)]

    # '#' の cost が x のとき、startからgoalの距離が t 以下になるかをDijkstra
    def check(x):
        dist=[INF]*n
        dist[s]=0
        visited=[0]*n
        for _ in range(n-1):
            v=min((dist[v],v) for v in range(n) if(not visited[v]))[1]
            visited[v]=1
            i,j=v//w,v%w
            for di,dj in D:
                ni,nj=i+di,j+dj
                if(not 0<=ni<h): continue
                if(not 0<=nj<w): continue
                nv=ni*w+nj
                if(dist[nv]>dist[v]+(x if(G[nv]=='#') else 1)):
                    dist[nv]=dist[v]+(x if(G[nv]=='#') else 1)
        return dist[g]<=t

    print(bisection(1,t,check))
resolve()

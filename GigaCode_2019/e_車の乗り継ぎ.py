# https://atcoder.jp/contests/gigacode-2019/tasks/gigacode_2019_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,l=map(int,input().split())
    E=[[] for _ in range(n+2)] # 0,x1,...,xn,l
    v,d=map(int,input().split())
    XVD=[None]*(n+1)
    XVD[0]=(0,v,d)
    for i in range(n):
        XVD[i+1]=tuple(map(int,input().split()))
    XVD.append((l,0,0))
    XVD.sort()

    for i in range(n+1):
        x0,v0,d0=XVD[i]
        for j in range(i+1,n+2):
            x1,v1,d1=XVD[j]
            if(x1-x0<=d0):
                E[i].append((j,(x1-x0)/v0))

    # dijkstra
    dist=[INF]*(n+2)
    dist[0]=0
    visited=[0]*(n+2)
    for _ in range(n+2):
        v=min((dist[v],v) for v in range(n+2) if(not visited[v]))[1]
        visited[v]=1
        for nv,w in E[v]:
            if(dist[nv]>dist[v]+w):
                dist[nv]=dist[v]+w
    ans=dist[-1]
    if(ans==INF):
        print('impossible')
        return
    print('{:.10f}'.format(ans))
resolve()

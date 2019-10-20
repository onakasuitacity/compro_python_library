# https://atcoder.jp/contests/abc143/tasks/abc143_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m,L=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(m):
        a,b,c=map(int,input().split())
        if(c>L): continue
        a-=1; b-=1
        E[a].append((b,c))
        E[b].append((a,c))
    A=[0]*n
    # pure Dijkstraを全ての始点で行う
    for u in range(n):
        dist=[(INF,INF)]*n # (補給回数,使用燃料)
        dist[u]=(0,0)
        calculated=[False]*n
        for _ in range(n-1):
            v=min((dist[v],v) for v in range(n) if(not calculated[v]))[1]
            calculated[v]=True
            now=dist[v]
            for nv,w in E[v]:
                if(now[1]+w<=L):
                    next=(now[0],now[1]+w)
                else:
                    next=(now[0]+1,w)
                if(dist[nv]>next):
                    dist[nv]=next
        A[u]=dist
    # output
    Q=int(input())
    for _ in range(Q):
        s,t=map(int,input().split())
        s-=1; t-=1
        ans=A[s][t][0]
        print(ans if ans!=INF else -1)
resolve()

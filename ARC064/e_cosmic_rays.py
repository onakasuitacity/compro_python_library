# https://atcoder.jp/contests/arc064/tasks/arc064_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from itertools import product
def resolve():
    xs,ys,xt,yt=map(int,input().split())
    n=int(input())
    CR=[None]*(n+2) # center, radius
    CR[0]=(xs+ys*1j,0)
    CR[n+1]=(xt+yt*1j,0)
    for i in range(1,n+1):
        x,y,r=map(int,input().split())
        CR[i]=(x+y*1j,r)

    # 各点の距離を求める
    n+=2
    E=[[] for _ in range(n)]
    for i,j in product(range(n),repeat=2):
        if(i>=j): continue
        c0,r0=CR[i]
        c1,r1=CR[j]
        d=max(0,abs(c0-c1)-r0-r1)
        E[i].append((j,d))
        E[j].append((i,d))

    # pure Dijkstra で 0 から n-1 の距離を計算する
    dist=[INF]*n
    dist[0]=0
    used=[0]*n
    for _ in range(n-1):
        v=min((dist[v],v) for v in range(n) if(not used[v]))[1]
        used[v]=1
        for nv,w in E[v]:
            if(dist[nv]>dist[v]+w):
                dist[nv]=dist[v]+w

    print(dist[-1])
resolve()

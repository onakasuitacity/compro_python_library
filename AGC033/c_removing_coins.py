# https://atcoder.jp/contests/agc033/tasks/agc033_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from collections import deque
def resolve():
    n=int(input())
    E=[[] for _ in range(n)]
    for i in range(n-1):
        a,b=map(int,input().split())
        a-=1; b-=1
        E[a].append(b)
        E[b].append(a)

    # double sweepで直径を求める
    dist=[INF]*n
    dist[0]=0
    Q=deque([0])
    while(Q):
        v=Q.popleft()
        for nv in E[v]:
            if(dist[nv]!=INF): continue
            dist[nv]=dist[v]+1
            Q.append(nv)

    v=max((dist[v],v) for v in range(n))[1]
    dist=[INF]*n
    dist[v]=0
    Q=deque([v])
    while(Q):
        v=Q.popleft()
        for nv in E[v]:
            if(dist[nv]!=INF): continue
            dist[nv]=dist[v]+1
            Q.append(nv)

    dia=max(dist)
    print("Second" if(dia%3==1) else "First")
resolve()

# https://atcoder.jp/contests/arc005/tasks/arc005_3
# PyPyだとMLE
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from itertools import product
from collections import deque
def resolve():
    h,w=map(int,input().split())
    G=[input() for _ in range(h)]
    for i,j in product(range(h),range(w)):
        if(G[i][j]=='s'): break
    si,sj=i,j
    for i,j in product(range(h),range(w)):
        if(G[i][j]=='g'): break
    ti,tj=i,j

    # 0-1 BFS
    dist=[[INF]*w for _ in range(h)]
    dist[si][sj]=0
    D=[(-1,0),(1,0),(0,-1),(0,1)]
    Q=deque([(si,sj)])
    while(Q):
        i,j=Q.popleft()
        for di,dj in D:
            ni,nj=i+di,j+dj
            if(not (0<=ni<h and 0<=nj<w)): continue
            d=1 if(G[ni][nj]=='#') else 0
            if(dist[ni][nj]>dist[i][j]+d):
                dist[ni][nj]=dist[i][j]+d
                if(d==0): Q.appendleft((ni,nj))
                else: Q.append((ni,nj))

    print("YES" if(dist[ti][tj]<=2) else "NO")
resolve()

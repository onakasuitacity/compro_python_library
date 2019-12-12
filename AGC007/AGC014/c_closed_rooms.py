# https://atcoder.jp/contests/agc014/tasks/agc014_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from itertools import product
from collections import deque
def resolve():
    h,w,k=map(int,input().split())
    G=[list(input()) for _ in range(h)]
    D=[(1,0),(-1,0),(0,1),(0,-1)]
    for i,j in product(range(h),range(w)):
        if(G[i][j]=='S'):
            i0,j0=i,j
            break

    dist=[[INF]*w for _ in range(h)]
    dist[i0][j0]=0
    # BFS
    Q=deque([(i0,j0)])
    while(Q):
        i,j=Q.popleft()
        for di,dj in D:
            ni=i+di; nj=j+dj
            if(not (0<=ni<h and 0<=nj<w)): continue
            if(dist[ni][nj]!=INF or G[ni][nj]=='#'): continue
            dist[ni][nj]=dist[i][j]+1
            Q.append((ni,nj))

    # 後は距離が k 以下の点から一直線に外に向かえばよい
    ans=INF
    for i,j in product(range(h),range(w)):
        if(dist[i][j]<=k):
            d=min(i,j,h-i-1,w-j-1)
            if(d==0):
                print(1)
                return
            else:
                ans=min(ans,2+(d-1)//k)
    print(ans)
resolve()

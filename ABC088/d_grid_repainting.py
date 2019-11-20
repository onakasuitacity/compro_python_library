# https://atcoder.jp/contests/abc088/tasks/abc088_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    h,w=map(int,input().split())
    grid=[None]*(h+2)
    grid[0]=['#']*(w+2)
    grid[-1]=['#']*(w+2)
    for i in range(1,h+1):
        grid[i]=list('#'+input()+'#')

    # startは(1,1) goalは(h,w)
    dist=[[INF]*(w+1) for _ in range(h+1)]
    dist[1][1]=1
    from collections import deque
    from itertools import product

    # BFS
    Q=deque([(1,1)])
    while(Q):
        i,j=Q.popleft()
        # 上下左右の4方向をcheck
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            if(grid[i+di][j+dj]=='#'): continue
            if(dist[i+di][j+dj]!=INF): continue
            dist[i+di][j+dj]=dist[i][j]+1
            Q.append((i+di,j+dj))

    if(dist[h][w]==INF):
        print(-1)
        return

    cnt=0
    for i in range(1,h+1):
        for j in range(1,w+1):
            cnt+=grid[i][j]=='.'
    print(cnt-dist[h][w])
resolve()

# https://atcoder.jp/contests/atc002/tasks/abc007_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    r,c=map(int,input().split())
    si,sj=map(lambda x:int(x)-1,input().split())
    gi,gj=map(lambda x:int(x)-1,input().split())
    grid=[list(input()) for _ in range(r)]

    d=[[INF]*c for _ in range(r)]
    d[si][sj]=0
    D=[(-1,0),(1,0),(0,-1),(0,1)]
    from collections import deque
    Q=deque([(si,sj)])
    while(Q):
        i,j=Q.popleft()
        for di,dj in D:
            if(d[i+di][j+dj]!=INF): continue
            if(grid[i+di][j+dj]=='#'): continue
            d[i+di][j+dj]=d[i][j]+1
            Q.append((i+di,j+dj))
    print(d[gi][gj])
resolve()

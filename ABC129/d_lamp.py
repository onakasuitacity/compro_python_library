# https://atcoder.jp/contests/abc129/tasks/abc129_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    h,w=map(int,input().split())
    grid=[0]*h
    for i in range(h):
        grid[i]=input()
    Sl=[[0]*w for _ in range(h)]
    Sr=[[0]*w for _ in range(h)]
    Su=[[0]*w for _ in range(h)]
    Sd=[[0]*w for _ in range(h)]

    # Sl
    for i in range(h):
        cnt=0
        for j in range(w):
            if(grid[i][j]=='.'):
                cnt+=1
                Sl[i][j]=cnt
            else:
                cnt=0
                Sl[i][j]=cnt

    # Sr
    for i in range(h):
        cnt=0
        for j in range(w-1,-1,-1):
            if(grid[i][j]=='.'):
                cnt+=1
                Sr[i][j]=cnt
            else:
                cnt=0
                Sr[i][j]=cnt

    # Su
    for j in range(w):
        cnt=0
        for i in range(h):
            if(grid[i][j]=='.'):
                cnt+=1
                Su[i][j]=cnt
            else:
                cnt=0
                Su[i][j]=cnt

    # Sd
    for j in range(w):
        cnt=0
        for i in range(h-1,-1,-1):
            if(grid[i][j]=='.'):
                cnt+=1
                Sd[i][j]=cnt
            else:
                cnt=0
                Sd[i][j]=cnt

    ans=0
    for i in range(h):
        for j in range(w):
            if(grid[i][j]=='#'): continue
            ans=max(Sl[i][j]+Sr[i][j]+Su[i][j]+Sd[i][j]-3,ans)
    print(ans)
resolve()

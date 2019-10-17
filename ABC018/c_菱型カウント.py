# https://atcoder.jp/contests/abc018/tasks/abc018_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    R,C,K=map(int,input().split())
    grid=[input() for _ in range(R)]
    up=[[0]*C for _ in range(R)]
    down=[[0]*C for _ in range(R)]
    for j in range(C):
        count=0
        for i in range(R):
            if(grid[i][j]=='o'): count+=1
            else: count=0
            up[i][j]=count
    for j in range(C):
        count=0
        for i in range(R-1,-1,-1):
            if(grid[i][j]=='o'): count+=1
            else: count=0
            down[i][j]=count
    ans=0
    from itertools import product
    for x,y in product(range(K-1,R-K+1),range(K-1,C-K+1)):
        flag=True
        for i in range(K):
            if(min(up[x][y-i],up[x][y+i],down[x][y-i],down[x][y+i])<K-i):
                flag=False
                break
        ans+=flag
    print(ans)
resolve()

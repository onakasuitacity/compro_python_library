# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    h,w,k=map(int,input().split())
    grid=[list(input()) for _ in range(h)]
    now=1
    from itertools import product
    for i,j in product(range(h),range(w)):
        if(grid[i][j]=='#'):
            l=j; r=j
            while(l-1>=0 and grid[i][l-1]=='.'): l-=1
            while(r+1<=w-1 and grid[i][r+1]=='.'): r+=1
            u=i; d=i
            while(u-1>=0 and all(grid[u-1][j]=='.' for j in range(l,r+1))): u-=1
            while(d+1<=h-1 and all(grid[d+1][j]=='.' for j in range(l,r+1))): d+=1
            for s,t in product(range(u,d+1),range(l,r+1)):
                grid[s][t]=now
            now+=1
    for g in grid:
        print(*g)
resolve()

# https://atcoder.jp/contests/abc008/tasks/abc008_4
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from functools import lru_cache
def resolve():
    w,h=map(int,input().split())
    n=int(input())
    XY=[tuple(map(int,input().split())) for _ in range(n)]

    @lru_cache(None)
    def dfs(x0,y0,x1,y1)->int:
        res=0
        for x,y in XY:
            if(x0<=x<=x1 and y0<=y<=y1):
                score=0
                if(x0<=x-1 and y0<=y-1): score+=dfs(x0,y0,x-1,y-1)
                if(x0<=x-1 and y+1<=y1): score+=dfs(x0,y+1,x-1,y1)
                if(x+1<=x1 and y0<=y-1): score+=dfs(x+1,y0,x1,y-1)
                if(x+1<=x1 and y+1<=y1): score+=dfs(x+1,y+1,x1,y1)
                res=max(res,score+x1-x0+y1-y0+1)
        return res

    print(dfs(1,1,w,h))
resolve()

# https://atcoder.jp/contests/abc006/tasks/abc006_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    # x+y+z=n, 2x+3y+4z=m
    # x=3n-m+z,y=m-2n-2z
    n,m=map(int,input().split())
    for z in range(0,n+1):
        x=3*n-m+z
        y=m-2*n-2*z
        if x>=0 and y>=0:
            print(x,y,z)
            return
    else:
        print(-1,-1,-1)
resolve()

# https://atcoder.jp/contests/abc010/tasks/abc010_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    x0,y0,x1,y1,t,v=map(int,input().split())
    z0=x0+y0*1j; z1=x1+y1*1j
    for _ in range(int(input())):
        x,y=map(int,input().split())
        z=x+y*1j
        d=abs(z-z0)+abs(z-z1)
        if(v*t>=d):
            print("YES")
            return
    print("NO")
resolve()

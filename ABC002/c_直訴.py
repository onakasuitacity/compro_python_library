# https://atcoder.jp/contests/abc002/tasks/abc002_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    x0,y0,x1,y1,x2,y2=map(int,input().split())
    u=(x1-x0,y1-y0)
    v=(x2-x0,y2-y0)
    print(abs(u[0]*v[1]-u[1]*v[0])/2)
resolve()

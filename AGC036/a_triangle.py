# https://atcoder.jp/contests/agc036/tasks/agc036_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    s=int(input())
    x0=10**9
    y1=(s-1)//x0+1
    x1=1
    y0=x0*y1-s
    print(0,0,x0,y0,x1,y1)
resolve()

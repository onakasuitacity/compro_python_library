# https://atcoder.jp/contests/abc130/tasks/abc130_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    w,h,x,y=map(int,input().split())
    print(w*h/2,int(w==x*2 and h==y*2))
resolve()

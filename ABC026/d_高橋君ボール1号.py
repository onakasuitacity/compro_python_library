# https://atcoder.jp/contests/abc026/tasks/abc026_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b,c=map(int,input().split())
    import math
    f=lambda t:a*t+b*math.sin(c*math.pi*t)-100
    l=0; r=1000
    while(r-l>2.5*10**-12):
        h=(l+r)/2
        if f(h)>0: r=h
        elif f(h)<0: l=h
        else:
            print(h)
            return
    print(h)
resolve()

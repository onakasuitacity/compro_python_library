# https://atcoder.jp/contests/agc019/tasks/agc019_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from math import pi
from bisect import bisect_left
def resolve():
    x1,y1,x2,y2=map(int,input().split())
    if(x1>x2): x1,y1,x2,y2=x2,y2,x1,y1 # x1<=x2
    trans=False
    if(y1>y2):
        y1,y2=-y1,-y2 # y1<=y2
        trans=True

    n=int(input())
    XY=[]
    for i in range(n):
        x,y=map(int,input().split())
        if(trans): y=-y
        if(x1<=x<=x2 and y1<=y<=y2):
            XY.append((x,y))

    d=(x2-x1)+(y2-y1) # マンハッタン
    d*=100
    l=min(x2-x1,y2-y1)

    # XYのLISを求めて、その個数*(20-5pi)を引けばよい
    XY.sort()
    C=[INF]*(n+1)
    for x,y in XY:
        i=bisect_left(C,y)
        C[i]=y
    k=C.index(INF)
    # LISの数が l より大きい時 -> 1回は無駄にしてしまう
    if(k>l):
        d-=(k-1)*(20-5*pi)
        d+=10*pi-20
    else:
        d-=k*(20-5*pi)
    print(d)
resolve()

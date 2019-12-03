# https://atcoder.jp/contests/abc016/tasks/abc016_4
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from collections import namedtuple
def resolve():
    P=namedtuple('P',"x y")
    x0,y0,x1,y1=map(int,input().split())
    p0=P(x0,y0); p1=P(x1,y1)
    check1=lambda p:(p.y-p0.y)*(p1.x-p0.x)>(p1.y-p0.y)*(p.x-p0.x)

    n=int(input())
    XY=[P(*map(int,input().split())) for _ in range(n)]
    XY.append(XY[0])

    cnt=0
    for i in range(n):
        p2=XY[i]; p3=XY[i+1]
        check2=lambda p:(p.y-p2.y)*(p3.x-p2.x)>(p3.y-p2.y)*(p.x-p2.x)
        cnt+=((check1(p2)^check1(p3)) and (check2(p0)^check2(p1)))
    print(cnt//2+1)
resolve()

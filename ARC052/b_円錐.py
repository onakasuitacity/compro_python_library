# https://atcoder.jp/contests/arc052/tasks/arc052_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from math import pi
def resolve():
    n,q=map(int,input().split())
    XRH=[tuple(map(int,input().split())) for _ in range(n)]

    for _ in range(q):
        a,b=map(int,input().split())
        ans=0
        for x,r,h in XRH:
            # x>a にある体積から、x>b にある体積を引く
            V=pi*r*r*h/3
            if(a<=x): ca=1
            elif(a<=x+h): ca=((x+h-a)/h)**3
            else: ca=0

            if(b<=x): cb=1
            elif(b<=x+h): cb=((x+h-b)/h)**3
            else: cb=0

            ans+=(ca-cb)*V
        print(ans)
resolve()

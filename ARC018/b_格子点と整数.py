# https://atcoder.jp/contests/arc018/tasks/arc018_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from collections import namedtuple
P=namedtuple('P',"x y")
def resolve():
    n=int(input())
    XY=[P(*map(int,input().split())) for _ in range(n)]
    ans=0
    for i in range(n):
        p0=XY[i]
        for j in range(i+1,n):
            p1=XY[j]
            for k in range(j+1,n):
                p2=XY[k]
                val=(p1.x-p0.x)*(p2.y-p0.y)-(p2.x-p0.x)*(p1.y-p0.y)
                ans+=((val!=0) and (val%2==0))
    print(ans)
resolve()

# https://atcoder.jp/contests/arc050/tasks/arc050_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()
from itertools import product
def resolve():
    R,B=map(int,input().split())
    a,b=map(int,input().split())

    P=[(R//a,0),(0,B//b),((b*R-B)//(a*b-1),(a*B-R)//(a*b-1))]
    check=lambda u,v:u>=0 and v>=0 and a*u+v<=R and u+b*v<=B

    ans=0
    for p,q in P:
        for u,v in product(range(p-5,p+6),range(q-5,q+6)):
            if(check(u,v)): ans=max(ans,u+v)

    print(ans)
resolve()

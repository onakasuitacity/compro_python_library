# https://atcoder.jp/contests/abc045/tasks/arc061_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from itertools import product
from collections import defaultdict
def resolve():
    h,w,n=map(int,input().split())
    D=defaultdict(int)
    for _ in range(n):
        a,b=map(int,input().split())
        for i,j in product(range(a-1,a+2),range(b-1,b+2)):
            if(2<=i<=h-1 and 2<=j<=w-1):
                D[(i,j)]+=1

    ans=[0]*10
    for v in D.values():
        ans[v]+=1
    ans[0]=(h-2)*(w-2)-sum(ans)
    print(*ans,sep='\n')
resolve()

# https://atcoder.jp/contests/abc057/tasks/abc057_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from itertools import groupby
from math import factorial

def comb(n,k):
    if(k<0 or n<k): return 0
    return factorial(n)//(factorial(k)*factorial(n-k))

def resolve():
    n,a,b=map(int,input().split())
    V=list(map(int,input().split()))
    V.sort(reverse=1)
    m=sum(V[:a])/a
    print(m)

    cnt=0
    for key,iter in groupby(V):
        k=len(list(iter))
        if(cnt+k>=a): break
        cnt+=k

    ans=0
    if(cnt==0):
        for i in range(a-cnt,min(k,b-cnt)+1):
            ans+=comb(k,i)
    else:
        ans=comb(k,a-cnt)
    print(ans)
resolve()

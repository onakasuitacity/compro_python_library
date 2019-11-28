# https://atcoder.jp/contests/abc052/tasks/arc067_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

def prime_factorization(n):
    assert(n>1)
    factor=[]
    sqrt=int(n**.5)
    for d in range(2,sqrt+1):
        while(n%d==0):
            n//=d
            factor.append(d)
    if n!=1: factor.append(n)
    return factor

from collections import defaultdict

def resolve():
    n=int(input())
    C=defaultdict(int)
    for x in range(2,n+1):
        for p in prime_factorization(x):
            C[p]+=1
    ans=1
    for v in C.values():
        ans*=v+1
        ans%=MOD
    print(ans)
resolve()

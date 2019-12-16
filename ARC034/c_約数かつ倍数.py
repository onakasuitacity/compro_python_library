# https://atcoder.jp/contests/arc034/tasks/arc034_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

def prime_factorization(n):
    assert(n>1)
    factor=[]
    for d in range(2,int(n**.5)+1):
        while(n%d==0):
            n//=d
            factor.append(d)
    if n!=1: factor.append(n)
    return factor

from collections import defaultdict
def resolve():
    a,b=map(int,input().split())
    if(a<b):
        print(0)
        return

    D=defaultdict(int)
    for x in range(b+1,a+1):
        for p in prime_factorization(x):
            D[p]+=1

    ans=1
    for k in D.values():
        ans*=k+1
        ans%=MOD
    print(ans)
resolve()

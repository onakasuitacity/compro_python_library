# https://atcoder.jp/contests/abc132/tasks/abc132_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from math import factorial
    n,k=map(int,input().split())
    def modfact(n):
        fact=[1]*(n+1)
        invfact=[1]*(n+1)
        for i in range(1,n+1):
            fact[i]=i*fact[i-1]%MOD
        invfact[n]=pow(fact[n],MOD-2,MOD)
        for i in range(n-1,-1,-1):
            invfact[i]=invfact[i+1]*(i+1)%MOD
        return fact,invfact
    fact,invfact=modfact(n)

    for i in range(1,k+1):
        if(n-k-i+1<0):
            print(0)
            continue
        ans=fact[k-1]*invfact[i-1]*invfact[k-i]
        print(ans*fact[n-k+1]*invfact[i]*invfact[n-k-i+1]%MOD)
resolve()

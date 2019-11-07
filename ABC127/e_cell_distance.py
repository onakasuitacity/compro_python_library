# https://atcoder.jp/contests/abc127/tasks/abc127_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def modfact(n):
    fact=[1]*(n+1)
    invfact=[1]*(n+1)
    for i in range(1,n+1):
        fact[i]=i*fact[i-1]%MOD
    invfact[n]=pow(fact[n],MOD-2,MOD)
    for i in range(n-1,-1,-1):
        invfact[i]=invfact[i+1]*(i+1)%MOD
    return fact,invfact

def resolve():
    n,m,k=map(int,input().split())
    fact,invfact=modfact(n*m-2)
    ans=1
    ans*=fact[m*n-2]*invfact[k-2]*invfact[m*n-k]
    ans*=((n-1)*n*(n+1)*m*m+(m-1)*m*(m+1)*n*n)//6
    print(ans%MOD)
resolve()

# https://atcoder.jp/contests/abc145/tasks/abc145_d
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
    x,y=map(int,input().split())
    if((x+y)%3):
        print(0)
        return

    z=(x+y)//3
    if(x-z<0 or y-z<0):
        print(0)
        return
    
    fact,invfact=modfact(z)
    print(fact[z]*invfact[x-z]%MOD*invfact[y-z]%MOD)
resolve()

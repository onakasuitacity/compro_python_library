# https://atcoder.jp/contests/agc025/tasks/agc025_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=998244353
input=lambda:sys.stdin.readline().rstrip()

class modfact(object):
    def __init__(self,n):
        fact=[1]*(n+1); invfact=[1]*(n+1)
        for i in range(1,n+1): fact[i]=i*fact[i-1]%MOD
        invfact[n]=pow(fact[n],MOD-2,MOD)
        for i in range(n-1,-1,-1): invfact[i]=invfact[i+1]*(i+1)%MOD
        self.__fact=fact; self.__invfact=invfact

    def inv(self,n):
        assert(n>0)
        return self.__fact[n-1]*self.__invfact[n]%MOD

    def fact(self,n):
        return self.__fact[n]

    def invfact(self,n):
        return self.__invfact[n]

    def comb(self,n,k):
        if(k<0 or n<k): return 0
        return self.__fact[n]*self.__invfact[k]*self.__invfact[n-k]%MOD

    def perm(self,n,k):
        if(k<0 or n<k): return 0
        return self.__fact[n]*self.__invfact[n-k]%MOD

from fractions import gcd
def resolve():
    n,a,b,k=map(int,input().split())

    # k=ax+by の不定方程式を解く
    g=gcd(a,b)
    if(k%g):
        print(0)
        return
    k//=g; a//=g; b//=g

    # k=ax+byの解は0<=x<b に1つだけある
    for x in range(b):
        if((k-a*x)%b==0):
            y=(k-a*x)//b
            break
    # 現在 x,y は k=ax+byを満たす x のうち、非負で最小のものとなっている
    # これを x,y -> x+b,y-a として iterate していく
    ans=0
    mf=modfact(n)
    while(y>=0):
        ans+=mf.comb(n,x)*mf.comb(n,y)
        x,y=x+b,y-a

    print(ans%MOD)
resolve()

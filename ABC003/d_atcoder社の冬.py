# https://atcoder.jp/contests/abc003/tasks/abc003_4
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
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
        return self.__fact[n]*self.__invfact[k]%MOD

def resolve():
    r,c=map(int,input().split())
    x,y=map(int,input().split())
    d,l=map(int,input().split())
    n=x*y

    mf=modfact(n)
    def tri(n):
        return mf.comb(n,d)*mf.comb(n-d,l)%MOD

    ans=tri(n)
    if(n!=d+l):
        ans-=2*tri(n-x)+2*tri(n-y)
        ans+=tri(n-2*x)+tri(n-2*y)+4*tri(n-x-y+1)
        ans-=2*tri(n-2*x-y+2)+2*tri(n-x-2*y+2)
        ans+=tri(n-2*x-2*y+4) # x,y=1,1 のときは例外処理が必要

    print(ans*(r-x+1)*(c-y+1)%MOD)
resolve()

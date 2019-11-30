# https://atcoder.jp/contests/abc042/tasks/arc058_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

class modfact(object):
    def __init__(self,n):
        fact=[1]*(n+1)
        invfact=[1]*(n+1)
        for i in range(1,n+1):
            fact[i]=i*fact[i-1]%MOD
        invfact[n]=pow(fact[n],MOD-2,MOD)
        for i in range(n-1,-1,-1):
            invfact[i]=invfact[i+1]*(i+1)%MOD
        self.__fact=fact
        self.__invfact=invfact

    def fact(self,n):
        return self.__fact[n]

    def invfact(self,n):
        return self.__invfact[n]

    def comb(self,n,k):
        if(k<0 or n-k<0): return 0
        return (self.fact(n)*self.invfact(k)*self.invfact(n-k))%MOD

def resolve():
    h,w,a,b=map(lambda x:int(x)-1,input().split())
    mf=modfact(h+w)
    ans=mf.comb(h+w,h)
    for j in range(b+1):
        i=(h-a)+b-j
        ans-=mf.comb(i+j,i)*mf.comb(h-i+w-j,h-i)%MOD
    print(ans%MOD)
resolve()

# https://atcoder.jp/contests/dp/tasks/dp_y
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
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

def resolve():
    h,w,n=map(int,input().split())
    RC=[None]*n
    for i in range(n):
        r,c=map(int,input().split())
        r-=1; c-=1
        RC[i]=(r,c)
    RC.append((h-1,w-1))
    n+=1
    RC.sort(lambda p:sum(p))

    mf=modfact(h+w)
    f=lambda x,y:mf.comb(x+y,x)
    dp=[None]*n
    for i in range(n):
        r,c=RC[i]
        res=f(r,c)
        for j in range(i):
            r0,c0=RC[j]
            res-=dp[j]*f(r-r0,c-c0)
        dp[i]=res%MOD

    print(dp[-1])
resolve()

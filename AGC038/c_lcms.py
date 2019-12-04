# https://atcoder.jp/contests/agc038/tasks/agc038_c
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
        self.__fact[n]*self.__invfact[k]%MOD

def prime(n):
    if(n<=1): return []
    S=[1]*(n+1)
    S[0]=0; S[1]=0
    for i in range(2,n):
        if(S[i]==0): continue
        for j in range(2*i,n+1,i): S[j]=0
    return [p for p in range(n+1) if(S[p])]

def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    V=max(A)
    C=[0]*(V+1)
    for a in A:
        C[a]+=1

    P=prime(V)
    W=[1]*(V+1)
    for p in P:
        for i in range(p,V+1,p):
            W[i]*=(1-p)
    mf=modfact(V)
    for i in range(1,V+1):
        W[i]=(W[i]*mf.inv(i))%MOD

    ans=0
    for d in range(1,V+1):
        s=0 # 和(後に2乗する)
        t=0 # 2乗の和
        for i in range(d,V+1,d):
            s+=i*C[i]
            t+=(i**2)*C[i]
        ans+=W[d]*(s**2-t)//2
        ans%=MOD
    print(ans)
resolve()

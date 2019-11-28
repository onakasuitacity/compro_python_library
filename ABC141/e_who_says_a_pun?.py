# https://atcoder.jp/contests/abc141/tasks/abc141_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

class RollingHash(object):
    __base1=1007; __mod1=10**9+9
    __base2=1009; __mod2=10**9+7

    def __init__(self,s):
        self.__s=s; self.__n=len(s)
        b1=self.__base1; m1=self.__mod1
        b2=self.__base2; m2=self.__mod2
        H1,H2=[0]*(self.__n+1),[0]*(self.__n+1)
        P1,P2=[1]*(self.__n+1),[1]*(self.__n+1)
        for i in range(self.__n):
            H1[i+1]=(H1[i]*b1+ord(s[i]))%m1
            H2[i+1]=(H2[i]*b2+ord(s[i]))%m2
            P1[i+1]=P1[i]*b1%m1
            P2[i+1]=P2[i]*b2%m2
        self.__H1=H1; self.__H2=H2
        self.__P1=P1; self.__P2=P2

    def __getitem__(self,x):
        if(isinstance(x,int)): x=slice(x,x+1)
        assert(isinstance(x,slice) and ((x.step is None) or (x.step==1)))
        l=x.start; r=x.stop;
        assert(l<=r)
        return ((self.__H1[r]-self.__P1[r-l]*self.__H1[l]%self.__mod1)%self.__mod1,
                (self.__H2[r]-self.__P2[r-l]*self.__H2[l]%self.__mod2)%self.__mod2)

def bisection(l,r,f,left=True,discrete=True):
    eps=1 if discrete else 10**-12
    if((not left)^f(r)): return r if left else r+1
    elif(left^f(l)): return l-1 if left else l
    while(r-l>eps):
        h=(l+r)//2 if discrete else (l+r)/2
        if((not left)^f(h)): l=h
        else: r=h
    return (l+r)/2 if not discrete else l if left else r

def resolve():
    n=int(input())
    S=input()
    rh=RollingHash(S)

    from collections import defaultdict
    def check(k):
        D=defaultdict(lambda :-1)
        for i in range(n-k+1):
            hash=rh[i:i+k]
            if(D[hash]!=-1):
                if(i-D[hash]>=k): return True
            else:
                D[hash]=i
        return False

    print(bisection(0,n,check))
resolve()

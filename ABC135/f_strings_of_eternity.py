# https://atcoder.jp/contests/abc135/tasks/abc135_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
class UnionFind(object):
    def __init__(self,n):
        self.__par=list(range(n))
        self.__rank=[0]*n
        self.__size=[1]*n

    def root(self,k):
        if(self.__par[k]==k): return k
        self.__par[k]=self.root(self.__par[k])
        return self.__par[k]

    def unite(self,i,j):
        i=self.root(i); j=self.root(j)
        par=self.__par; rank=self.__rank; size=self.__size
        if(i==j): return False
        if(rank[i]>rank[j]):
            par[j]=i
            size[i]+=size[j]
        else:
            par[i]=j
            size[j]+=size[i]
            if(rank[i]==rank[j]): rank[j]+=1
        return True

    def size(self,k):
        return self.__size[self.root(k)]

class RollingHash(object):
    __base1=1007; __mod1=10**9+9
    __base2=1009; __mod2=10**9+7

    def __init__(self,s):
        n=len(s)
        self.__s=s
        self.__n=n
        b1=self.__base1; m1=self.__mod1
        b2=self.__base2; m2=self.__mod2
        H1,H2=[0]*(n+1),[0]*(n+1)
        P1,P2=[1]*(n+1),[1]*(n+1)
        for i in range(n):
            H1[i+1]=(H1[i]*b1+ord(s[i]))%m1
            H2[i+1]=(H2[i]*b2+ord(s[i]))%m2
            P1[i+1]=P1[i]*b1%m1
            P2[i+1]=P2[i]*b2%m2
        self.__H1=H1; self.__H2=H2
        self.__P1=P1; self.__P2=P2

    def hash(self,l,r):
        m1=self.__mod1; m2=self.__mod2
        assert 0<=l<=r<=self.__n
        return ((self.__H1[r]-self.__P1[r-l]*self.__H1[l]%m1)%m1,
                (self.__H2[r]-self.__P2[r-l]*self.__H2[l]%m2)%m2)

def resolve():
    from math import ceil
    s=input()
    t=input()
    n=len(s)
    m=len(t)
    s=s*ceil(m/n)
    s=s*2

    ok=[0]*n
    uf=UnionFind(n)
    rhs=RollingHash(s)
    rht=RollingHash(t)
    t=rht.hash(0,m)
    for i in range(n):
        if(rhs.hash(i,i+m)==t):
            ok[i]=1
    for i in range(n):
        if(ok[i] and ok[(i+m)%n]):
            if(not uf.unite(i,(i+m)%n)):
                print(-1)
                return
    ans=0
    for i in range(n):
        if(ok[i]): ans=max(ans,uf.size(i))
    print(ans)
resolve()

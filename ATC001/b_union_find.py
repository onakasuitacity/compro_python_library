# https://atcoder.jp/contests/atc001/tasks/unionfind_a
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

    def is_same(self,i,j):
        return self.root(i)==self.root(j)

    def size(self,k):
        return self.__size[self.root(k)]

def resolve():
    n,q=map(int,input().split())
    uf=UnionFind(n)
    for _ in range(q):
        p,a,b=map(int,input().split())
        a-=1; b-=1
        if(p==0):
            uf.unite(a,b)
        else:
            print("Yes" if(uf.is_same(a,b)) else "No")
resolve()

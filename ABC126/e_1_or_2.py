# https://atcoder.jp/contests/abc126/tasks/abc126_e
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

def resolve():
    n,m=map(int,input().split())
    uf=UnionFind(n)
    for _ in range(m):
        x,y,z=map(int,input().split())
        x-=1; y-=1
        uf.unite(x,y)
    print(len({uf.root(i) for i in range(n)}))
resolve()

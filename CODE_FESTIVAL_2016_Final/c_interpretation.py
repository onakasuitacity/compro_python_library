# https://atcoder.jp/contests/cf16-final/tasks/codefestival_2016_final_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

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
    n,m=map(int,input().split())
    uf=UnionFind(m)
    S=set()
    for _ in range(n):
        L=list(map(int,input().split()))[::-1]
        k=L.pop()
        for i in range(k):
            S.add(L[i]-1)
            if(i+1<k):
                uf.unite(L[i]-1,L[i+1]-1)

    print("YES" if(max(uf.size(i) for i in range(m))==len(S)) else "NO")
resolve()

# https://atcoder.jp/contests/abc120/tasks/abc120_d
class UnionFind(object):
    """
    query: O(Ack^-1(n,n)) (amortize)
    """
    def __init__(self,n):
        """
        param n: number of nodes
        """
        self.__par=list(range(n))
        self.__rank=[0]*n
        self.__size=[1]*n

    def __root(self,k):
        if self.__par[k]==k: return k
        else:
            self.__par[k]=self.__root(self.__par[k])
            return self.__par[k]

    def is_same(self,i,j):
        return self.__root(i)==self.__root(j)

    def unite(self,i,j):
        i=self.__root(i)
        j=self.__root(j)
        if i==j: return
        if self.__rank[i]>self.__rank[j]:
            self.__par[j]=i
            self.__size[i]+=self.__size[j]
        else:
            self.__par[i]=j
            self.__size[j]+=self.__size[i]
            if self.__rank[i]==self.__rank[j]: self.__rank[j]+=1

    def size(self,k):
        return self.__size[self.__root(k)]

import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
# input=sys.stdin.readline
def resolve():
    n,m=map(int,input().split())
    ab=[map(int,input().split()) for _ in range(m)]
    tree=UnionFind(n)
    ans=[0]*m
    score=n*(n-1)//2
    ans[m-1]=score
    for i in range(m-1,0,-1):
        a,b=ab[i]
        a,b=a-1,b-1
        if not tree.is_same(a,b):
            score-=tree.size(a)*tree.size(b)
            tree.unite(a,b)
        ans[i-1]=score
    print(*ans,sep='\n')

resolve()

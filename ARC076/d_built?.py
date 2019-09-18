# https://atcoder.jp/contests/arc076/tasks/arc076_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
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
            else:
                self.__par[i]=j
                if self.__rank[i]==self.__rank[j]: self.__rank[j]+=1

    # Kruskal's algorithm
    from operator import itemgetter
    n=int(input())
    P=[0]*n
    edges=[0]*(2*n-2)
    for i in range(n):
        x,y=map(int,input().split())
        P[i]=(x,y,i)
    # xでsort
    P.sort(key=itemgetter(0))
    for k in range(n-1):
        x0,y0,i=P[k]
        x1,y1,j=P[k+1]
        edges[k]=(i,j,min(abs(x0-x1),abs(y0-y1)))
    # yでsort
    P.sort(key=itemgetter(1))
    for k in range(n-1):
        x0,y0,i=P[k]
        x1,y1,j=P[k+1]
        edges[k+n-1]=(i,j,min(abs(x0-x1),abs(y0-y1)))
    # edgesをcostでsort
    edges.sort(key=itemgetter(2))
    # union findに突っ込んでいく
    tree=UnionFind(n)
    ans=0
    for i,j,cost in edges:
        if tree.is_same(i,j): continue
        tree.unite(i,j)
        ans+=cost
    print(ans)
resolve()

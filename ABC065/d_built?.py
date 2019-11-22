# https://atcoder.jp/contests/abc065/tasks/arc076_b
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
    n=int(input())
    XYI=[0]*n
    for i in range(n):
        x,y=map(int,input().split())
        XYI[i]=(x,y,i)

    # Kruskal に使う可能性のある辺だけをグラフに追加する
    E=[]
    XYI.sort()
    for i in range(n-1):
        x0,y0,u=XYI[i]
        x1,y1,v=XYI[i+1]
        E.append((u,v,x1-x0))
    XYI.sort(lambda x:x[1])
    for i in range(n-1):
        x0,y0,u=XYI[i]
        x1,y1,v=XYI[i+1]
        E.append((u,v,y1-y0))

    # Kruskal method
    E.sort(lambda x:x[2])
    uf=UnionFind(n)
    ans=0
    for u,v,w in E:
        if(uf.unite(u,v)):
            ans+=w
    print(ans)
resolve()

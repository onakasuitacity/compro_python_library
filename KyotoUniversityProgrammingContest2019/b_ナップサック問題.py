# https://atcoder.jp/contests/kupc2019/tasks/kupc2019_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.buffer.readline().rstrip()
class UnionFind(object):
    def __init__(self,n,size):
        self.__par=list(range(n))
        self.__rank=[0]*n
        self.__size=size

    def root(self,k):
        if(self.__par[k]==k): return k
        self.__par[k]=self.root(self.__par[k])
        return self.__par[k]

    def unite(self,i,j):
        i=self.root(i); j=self.root(j)
        par=self.__par; rank=self.__rank; size=self.__size
        if(i==j): return
        s=(size[i][0]+size[j][0],size[i][1]+size[j][1])
        if(rank[i]>rank[j]):
            par[j]=i
            size[i]=s
        else:
            par[i]=j
            size[j]=s
            if(rank[i]==rank[j]): rank[j]+=1

    def size(self,k):
        return self.__size[self.root(k)]

def resolve():
    n,m,W=map(int,input().split())
    size=[0]*n
    for i in range(n):
        size[i]=tuple(map(int,input().split()))
    uf=UnionFind(n,size)
    for _ in range(m):
        uf.unite(*map(lambda x:int(x)-1,input().split()))
    s={uf.root(i) for i in range(n)}
    n=len(s)
    s=list(s)
    dp=[[0]*(W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        w,v=uf.size(s.pop())
        for k in range(W+1):
            if(k-w>=0): dp[i][k]=max(dp[i-1][k-w]+v,dp[i-1][k])
            else: dp[i][k]=dp[i-1][k]
    print(dp[n][W])
resolve()

# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

class UnionFind(object):
    def __init__(self,n):
        self.__par=list(range(n))
        self.__size=[1]*n

    def root(self,k):
        if(self.__par[k]==k): return k
        self.__par[k]=self.root(self.__par[k])
        return self.__par[k]

    def unite(self,i,j):
        i=self.root(i); j=self.root(j)
        if(i==j): return False
        par=self.__par; size=self.__size
        if(size[i]<size[j]): i,j=j,i
        par[j]=i
        size[i]+=size[j]
        return True

    def is_same(self,i,j):
        return self.root(i)==self.root(j)

    def size(self,i):
        return self.__size[self.root(i)]

from itertools import product
from operator import itemgetter
def resolve():
    h,w=map(int,input().split())
    G=[input()+'#' for _ in range(h)]
    G.append('#'*(w+1))

    dp=[[0]*(w+1) for _ in range(h+1)]
    for i,j in product(range(h-1,-1,-1),range(w-1,-1,-1)):
        if(G[i][j]=='#'): continue
        dp[i][j]=min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])+1

    # grid を 1-dim とみなし、dp の値順に辺を保持する
    C=[[] for _ in range(min(h,w)+1)]
    for i,j in product(range(h),range(w)): # 下と右とに辺を張る
        if(dp[i][j]==0): continue
        x=i*w+j
        if(i+1<h and dp[i+1][j]!='#'): C[min(dp[i][j],dp[i+1][j])].append((x,x+w))
        if(j+1<w and dp[i][j+1]!='#'): C[min(dp[i][j],dp[i][j+1])].append((x,x+1))

    # query を先読みし、L の大きい順に処理
    q=int(input())
    VLI=[None]*q
    for i in range(q):
        x,y,l=map(int,input().split())
        x-=1; y-=1
        VLI[i]=(x*w+y,l,i)
    VLI.sort(itemgetter(1),reverse=1)

    # query を処理
    ans=[None]*q
    now=min(h,w)
    uf=UnionFind(h*w)
    for v,l,i in VLI:
        while(now>=l):
            for x,y in C[now]:
                uf.unite(x,y)
            now-=1
        ans[i]=uf.size(v)

    # output
    print(*ans,sep='\n')
resolve()

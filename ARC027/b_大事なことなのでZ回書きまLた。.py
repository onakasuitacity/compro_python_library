# https://atcoder.jp/contests/arc027/tasks/arc027_2
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
    n=int(input())
    S1=input()
    S2=input()
    S=(set(S1)|set(S2))-set(map(str,range(10)))
    idx={s:i for i,s in enumerate(S)}
    k=len(idx)

    uf=UnionFind(k)
    # まずは双方でアルファベットのものを unite する
    for s1,s2 in zip(S1,S2):
        if(s1 in S and s2 in S):
            uf.unite(idx[s1],idx[s2])
    V={uf.root(i):0 for i in range(k)}
    # 次に先頭が双方アルファベットの場合は 0 を除外する
    if(S1[0] in S and S2[0] in S):
        V[uf.root(idx[S1[0]])]=-1
    # 最後に片方がアルファベットで片方が数字のものを確定させる
    for s1,s2 in zip(S1,S2):
        if((s1 in S)^(s2 in S)):
            if(s1 in S):
                V[uf.root(idx[s1])]=1
            else:
                V[uf.root(idx[s2])]=1

    ans=1
    for val in V.values():
        if(val==0): ans*=10
        elif(val==-1): ans*=9
    print(ans)
resolve()

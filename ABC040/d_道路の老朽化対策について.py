# https://atcoder.jp/contests/abc040/tasks/abc040_d
class UnionFind(object):
    def __init__(self,n):
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
        k=self.__root(k)
        return self.__size[k]

import sys
input=sys.stdin.readline
def resolve():
    n,m=map(int,input().split())
    uf=UnionFind(n+1)
    A=[tuple(map(int,input().split())) for _ in range(m)]
    q=int(input())
    for i in range(q):
    # 人の番号を-1,-2,...で保存しておく
        v,w=map(int,input().split())
        A.append((~i,v,w))
    A.sort(key=lambda x:x[0])
    A.sort(key=lambda x:x[2],reverse=1)
    ans=[0]*q
    for a,b,y in A:
        if a>0: # unite
            uf.unite(a,b)
        else: # query
            ans[~a]=uf.size(b)
    print(*ans,sep="\n")

resolve()

# https://atcoder.jp/contests/arc045/tasks/arc045_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

class SparseTable(object):
    def __init__(self,A):
        n=len(A)
        logn=max(1,(n-1).bit_length())
        maxtable=[[0]*n for _ in range(logn)]
        maxtable[0]=A[:]
        mintable=[[0]*n for _ in range(logn)]
        mintable[0]=A[:]
        from itertools import product
        for i,k in product(range(1,logn),range(n)):
            if(k+(1<<(i-1))>=n):
                maxtable[i][k]=maxtable[i-1][k]
                mintable[i][k]=mintable[i-1][k]
            else:
                maxtable[i][k]=max(maxtable[i-1][k],maxtable[i-1][k+(1<<(i-1))])
                mintable[i][k]=min(mintable[i-1][k],mintable[i-1][k+(1<<(i-1))])
        self.__n=n
        self.__maxtable=maxtable
        self.__mintable=mintable

    def max(self,l,r):
        n=self.__n
        assert 0<=l<r<=n
        i=max(0,(r-l-1).bit_length()-1)
        maxtable=self.__maxtable
        return max(maxtable[i][l],maxtable[i][r-(1<<i)])

    def min(self,l,r):
        n=self.__n
        assert 0<=l<r<=n
        i=max(0,(r-l-1).bit_length()-1)
        mintable=self.__mintable
        return min(mintable[i][l],mintable[i][r-(1<<i)])

def resolve():
    n,m=map(int,input().split())
    imos=[0]*(n+1)
    I=[None]*m
    for i in range(m):
        s,t=map(int,input().split())
        s-=1
        I[i]=(s,t)
        imos[s]+=1
        imos[t]-=1
    for i in range(n):
        imos[i+1]+=imos[i]

    imos.pop()
    table=SparseTable(imos)
    ans=[]
    for i in range(m):
        l,r=I[i]
        if(table.min(l,r)>=2):
            ans.append(i+1)

    print(len(ans))
    if(ans):
        print(*ans,sep='\n')
resolve()

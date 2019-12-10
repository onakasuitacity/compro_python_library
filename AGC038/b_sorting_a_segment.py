# https://atcoder.jp/contests/agc038/tasks/agc038_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

class SparseTable(object):
    def __init__(self,A):
        n=len(A)
        logn=max(0,(n-1).bit_length())
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
    n,k=map(int,input().split())
    P=list(map(int,input().split()))
    table=SparseTable(P)
    ans=n-k+1
    for i in range(n-k):
        m=table.min(i,i+k)
        M=table.max(i+1,i+1+k)
        if(m==P[i] and M==P[i+k]):
            ans-=1

    cnt=0
    num=0
    P.append(-1) # 番兵
    for i in range(n):
        if(P[i+1]>P[i]):
            cnt+=1
        else:
            num+=(cnt>=k-1)
            cnt=0
    ans-=max(num-1,0)
    print(ans)
resolve()

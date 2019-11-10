# https://atcoder.jp/contests/chokudai_s001/tasks/chokudai_S001_j
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
class BIT(object):
    def __init__(self,A,dot,e,inv=None):
        n=len(A)
        self.__n=n
        self.__dot=dot
        self.__e=e
        self.__inv=inv
        self.__node=['$']+A # 1-indexed
        for i in range(1,n+1):
            j=i+(i&-i)
            if(j<=n): self.__node[j]=dot(self.__node[i],self.__node[j])

    def add(self,i,w=1):
        i+=1
        while(i<=self.__n):
            self.__node[i]=self.__dot(self.__node[i],w)
            i+=i&-i

    def sum(self,i):
        i+=1
        res=self.__e
        while(i>0):
            res=self.__dot(res,self.__node[i])
            i-=i&-i
        return res


def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    from operator import add
    bit=BIT([0]*(n+3),add,0)
    cnt=0
    for i in range(n):
        cnt+=i-bit.sum(A[i])
        bit.add(A[i])
    print(cnt)
resolve()

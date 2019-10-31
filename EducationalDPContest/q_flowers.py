# https://atcoder.jp/contests/dp/tasks/dp_q
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

    def add(self,i,w):
        i+=1
        while(i<=self.__n):
            self.__node[i]=self.__dot(self.__node[i],w)
            i+=i&-i

    def sum(self,i):
        res=self.__e
        while(i>0):
            res=self.__dot(res,self.__node[i])
            i-=i&-i
        return res
def resolve():
    n=int(input())
    H=list(map(lambda x:int(x)-1,input().split()))
    A=list(map(int,input().split()))
    bit=BIT([0]*n,max,0)
    for i in range(n):
        bit.add(H[i],bit.sum(H[i])+A[i])
    print(bit.sum(n))
resolve()

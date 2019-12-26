# https://atcoder.jp/contests/arc075/tasks/arc075_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()

class BIT(object):
    def __init__(self,A,dot=lambda x,y:x+y,e=0,inv=None):
        n=len(A)
        self.__n=n; self.__dot=dot; self.__e=e; self.__inv=inv; self.__node=['$']+A
        for i in range(1,n+1):
            j=i+(i&-i)
            if(j<=n): self.__node[j]=dot(self.__node[i],self.__node[j])

    def add(self,i,w=1):
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

    def range_sum(self,l,r):
        assert(self.__inv)
        return self.__inv(self.sum(r),self.sum(l))

def resolve():
    n,k=map(int,input().split())
    A=[int(input())-k for i in range(n)]
    S=[0]*(n+1)
    for i in range(n):
        S[i+1]=S[i]+A[i]

    # S[i] の転倒数を考えれば良く、そのために座圧する
    D={s:i for i,s in enumerate(sorted(set(S)))}
    for i in range(n+1):
        S[i]=D[S[i]]

    ans=0
    bit=BIT([0]*(max(S)+1))
    for s in S:
        ans+=bit.sum(s+1)
        bit.add(s)

    print(ans)
resolve()

# https://atcoder.jp/contests/abc107/tasks/arc101_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
class BIT(object):
    def __init__(self,A,dot=lambda x,y:x+y,e=0,inv=None):
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
        res=self.__e
        while(i>0):
            res=self.__dot(res,self.__node[i])
            i-=i&-i
        return res

def bisection(l,r,f,left=True,discrete=True):
    eps=1 if discrete else 10**-12
    if((not left)^f(r)): return r if left else r+1
    elif(left^f(l)): return l-1 if left else l
    while(r-l>eps):
        h=(l+r)//2 if discrete else (l+r)/2
        if((not left)^f(h)): l=h
        else: r=h
    return (l+r)/2 if not discrete else l if left else r

def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    M=max(A)

    def check(x):
        B=[1 if(a>=x) else -1 for a in A]
        S=[0]*(n+1)
        for i in range(n):
            S[i+1]=S[i]+B[i]

        D={d:i for i,d in enumerate(sorted(set(S)))}
        for i in range(n+1):
            S[i]=D[S[i]]

        cnt=0
        bit=BIT([0]*(n+1))
        for i in range(n+1):
            cnt+=bit.sum(S[i]+1)
            bit.add(S[i])

        return cnt*2>=n*(n+1)//2

    print(bisection(0,M,check))
resolve()

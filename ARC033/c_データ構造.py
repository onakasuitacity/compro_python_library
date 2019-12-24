# https://atcoder.jp/contests/arc033/tasks/arc033_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
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

    def bisect_left(self,w,increase=True):
        n=self.__n
        k=2**((self.__n-1).bit_length())
        res=0
        now=self.__e
        while(k):
            if(res+k<=n and self.__dot(now,self.__node[res+k])<w and increase):
                now=self.__dot(now,self.__node[res+k])
                res+=k
            elif(res+k<=n and self.__dot(now,self.__node[res+k])>w and (not increase)):
                now=self.__dot(now,self.__node[res+k])
                res+=k
            k//=2
        return res

def resolve():
    tree=BIT([0]*200001)
    for _ in range(int(input())):
        t,x=map(int,input().split())
        if(t==1):
            tree.add(x,1)
        else:
            i=tree.bisect_left(x)
            print(i)
            tree.add(i,-1)
resolve()

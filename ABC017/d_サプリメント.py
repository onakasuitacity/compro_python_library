# https://atcoder.jp/contests/abc017/tasks/abc017_4
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

class SegmentTree(object):
    def __init__(self,A,dot,e):
        n=2**((len(A)-1).bit_length())
        self.__n=n
        self.__dot=dot
        self.__e=e
        self.__node=[e]*(2*n)
        for i in range(len(A)):
            self.__node[i+n]=A[i]
        for i in range(n-1,-0,-1):
            self.__node[i]=dot(self.__node[2*i],self.__node[2*i+1])

    def update(self,i,c):
        i+=self.__n
        node=self.__node
        node[i]=c
        while(i!=1):
            i//=2
            node[i]=self.__dot(node[2*i],node[2*i+1])

    def sum(self,l,r):
        vl,vr=self.__e,self.__e
        l+=self.__n; r+=self.__n
        while(l<r):
            if(l%2==1):
                vl=self.__dot(vl,self.__node[l])
                l+=1
            l//=2
            if(r%2==1):
                r-=1
                vr=self.__dot(self.__node[r],vr)
            r//=2
        return self.__dot(vl,vr)

def resolve():
    n,m=map(int,input().split())
    F=[int(input()) for _ in range(n)]
    ot=[None]*(n+1) # ot[v] : vに遷移できる最小の頂点
    S=set()
    u=n
    for v in range(n,0,-1):
        while(u>0 and F[u-1] not in S):
            S.add(F[u-1])
            u-=1
        ot[v]=u
        S.remove(F[v-1])

    F.insert(0,0)
    from operator import add
    tree=SegmentTree([0]*(n+1),add,0)
    tree.update(0,1)
    for v in range(1,n+1):
        s=tree.sum(ot[v],v)
        tree.update(v,s%MOD)

    print(tree.sum(n,n+1))
resolve()

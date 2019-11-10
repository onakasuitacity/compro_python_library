# https://atcoder.jp/contests/arc026/tasks/arc026_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
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

    def add(self,i,c):
        i+=self.__n
        node=self.__node
        node[i]=self.__dot(c,node[i])
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
    n,L=map(int,input().split())
    LRC=[0]*n
    for i in range(n):
        l,r,c=map(int,input().split())
        r+=1
        LRC[i]=(l,r,c)
    LRC.sort()

    A=[INF]*(L+1)
    A[0]=0
    tree=SegmentTree(A,min,INF)

    for l,r,c in LRC:
        s=tree.sum(l,r)
        tree.add(r-1,s+c)

    print(tree.sum(L,L+1))
resolve()

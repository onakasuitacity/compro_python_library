# https://atcoder.jp/contests/arc008/tasks/arc008_4
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

    def bisect(self,l,r,x,increase=True,i=1,a=0,b=-1):
        """
        if increase: return d such that S[i]<x iff i<=d (l<=i<l)
        else: S[i]>x iff i<=d
        where S is cummulative sum of A
        """
        if b==-1: b=self.__n
        if increase:
            if self.__node[i]<=x or b<=l or r<=a: return -1
            if i>=self.__n: return i-self.__n
            lv=self.bisect(l,r,x,increase,2*i,a,(a+b)//2)
            if lv!=-1: return lv
            return self.bisect(l,r,x,increase,2*i+1,(a+b)//2,b)
        else:
            if self.__node[i]>=x or b<=l or r<=a: return -1
            if i>=self.__n: return i-self.__n
            rv=self.bisect(l,r,x,increase,2*i+1,(a+b)//2,b)
            if rv!=-1: return rv
            return self.bisect(l,r,x,increase,2*i,a,(a+b)//2)

import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    e=(1,0)
    dot=lambda a,b:(a[0]*b[0],a[1]*b[0]+b[1])
    Point=set()
    Query=[]
    for _ in range(m):
        p,a,b=input().split()
        p=int(p)-1
        a,b=float(a),float(b)
        Point.add(p)
        Query.append((p,a,b))
    # coordinate compression
    Point=sorted(Point)
    n=len(Point)
    id={Point[i]:i for i in range(n)}
    # segment tree
    A=[e]*n
    tree=SegmentTree(A,dot,e)
    res=[1]
    for p,a,b in Query:
        tree.update(id[p],(a,b))
        res.append(sum(tree.sum(0,n)))
    print(min(res))
    print(max(res))
resolve()

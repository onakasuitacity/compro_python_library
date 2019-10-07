# lazy-propagation segment tree
# http://tsutaj.hatenablog.com/entry/2017/03/30/224339
# http://beet-aizu.hatenablog.com/entry/2017/12/01/225955
# http://sugarknri.hatenablog.com/entry/2018/04/16/123016
# https://onedrive.live.com/View.aspx?resid=CD510BE428DBA1E7!106&authkey=!AFD6EO1-AReoPBk
class SegmentTree(object):
    def __init__(self,A,dot,e,comp,id,act):
        """
        A: array of monoid (M,dot,e)
        comp: composite function of Hom(M), comp(f,g)=gf
        id: identity map of M
        act: action on (Hom(M),M), act(f,a)=f(a)
        """
        n=2**((len(A)-1).bit_length())
        self.__n=n
        self.__dot=dot
        self.__e=e
        self.__comp=comp
        self.__id=id
        self.__act=act
        self.__node=[e]*(2*n-1)
        self.__lazy=[id]*(2*n-1)
        for i in range(len(A)):
            self.__node[n-1+i]=A[i]
        for i in range(n-2,-1,-1):
            self.__node[i]=dot(self.__node[2*i+1],self.__node[2*i+2])

    def __get_range(self,l,r):
        if l>=r: return [],[]
        Left,Right=[],[]
        n=self.__n
        l+=n-1; r+=n-2
        while(l<r):
            if l%2==0:
                Left.append(l)
            if r%2==1:
                Right.append(r)
                r-=1
            l=l//2; r=(r-1)//2
        if l==r:
            if l%2==0: Left.append(l)
            else: Right.append(l)
        return Left,Right

    def __propagate(self,i):
        if self.__lazy[i]==self.__id: return
        node=self.__node
        lazy=self.__lazy
        if i<=self.__n-2: # propagate to children
            lazy[2*i+1]=self.__comp(lazy[2*i+1],lazy[i])
            lazy[2*i+2]=self.__comp(lazy[2*i+2],lazy[i])
        node[i]=self.__act(lazy[i],node[i]) # action
        lazy[i]=self.__id

    def add(self,l,r,f):
        Left,Right=self.__get_range(l,r)
        lazy=self.__lazy
        for i in Left+Right:
            lazy[i]=self.__comp(lazy[i],f)
            self.__propagate(i)
        if l!=0 and Left: self.__propagate(Left[0]-1)
        if r!=self.__n and Right: self.__propagate(Right[0]+1)
        node=self.__node
        lowest=[]
        if Left: lowest.append(Left[0])
        if Right: lowest.append(Right[0])
        for i in lowest:
            while(i!=0):
                i=(i-1)//2
                node[i]=self.__dot(node[2*i+1],node[2*i+2])

    def sum(self,l,r):
        Left,Right=self.__get_range(l,r)
        for i in Left+Right: self.__propagate(i)
        res=self.__e
        for i in Left+Right[::-1]:
            res=self.__dot(res,self.__node[i])
        return res

    def bisect(self,l,r,x,increase=True,i=0,a=0,b=None):
        """
        if increase: return d such that S[i]<x iff i<=d (l<=i<l)
        else: S[i]>x iff i<=d
        where S is cummulative sum of A
        """
        self.__propagate(i)
        if b is None: b=self.__n
        if increase:
            if self.__node[i]<=x or b<=l or r<=a: return -1
            if i>=self.__n-1: return i-(self.__n-1)
            lv=self.bisect(l,r,x,increase,2*i+1,a,(a+b)//2)
            if lv!=-1: return lv
            return self.bisect(l,r,x,increase,2*i+2,(a+b)//2,b)
        else:
            if self.__node[i]>=x or b<=l or r<=a: return -1
            if i>=self.__n-1: return i-(self.__n-1)
            rv=self.bisect(l,r,x,increase,2*i+2,(a+b)//2,b)
            if rv!=-1: return rv
            return self.bisect(l,r,x,increase,2*i+1,a,(a+b)//2)


# RmQ and range add
INF=float("inf")
A=[4,9,11,5,13,33,33,33,11,45,14,19,19,8,10,89]
from operator import add
tree=SegmentTree(A,min,INF,add,0,add)
print(tree._SegmentTree__get_range(4,12))
tree.add(2,8,4)
print(tree.sum(1,5))
print(tree.bisect(3,13,9.5,increase=False))

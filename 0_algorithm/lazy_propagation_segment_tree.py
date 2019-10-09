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
            self.__node[i]=self.__dot(self.__node[2*i+1],self.__node[2*i+2])

    def __propagate(self,i):
        if self.__lazy[i]==self.__id: return
        node=self.__node
        lazy=self.__lazy
        if i<=self.__n-2: # propagate to children
            lazy[2*i+1]=self.__comp(lazy[2*i+1],lazy[i])
            lazy[2*i+2]=self.__comp(lazy[2*i+2],lazy[i])
        node[i]=self.__act(lazy[i],node[i]) # action
        lazy[i]=self.__id

    def __ancestors_propagate(self,i):
        if i==0: return
        i=(i-1)//2
        self.__ancestors_propagate(i)
        self.__propagate(i)

    def __update_ancestors(self,i):
        while(i!=0):
            self.__propagate(i-1+2*(i%2)) # propagate the sibling of i
            i=(i-1)//2
            self.__node[i]=self.__dot(self.__node[2*i+1],self.__node[2*i+2])

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

    def update(self,i,c):
        i+=self.__n-1
        self.__ancestors_propagate(i)
        self.__node[i]=c
        self.__update_ancestors(i)

    def add(self,l,r,f):
        Left,Right=self.__get_range(l,r)
        lowest=[]
        if Left: lowest.append(Left[0])
        if Right: lowest.append(Right[0])
        for i in lowest: self.__ancestors_propagate(i)
        for i in Left+Right:
            self.__lazy[i]=self.__comp(self.__lazy[i],f)
        for i in lowest:
            self.__propagate(i)
            self.__update_ancestors(i)

    def sum(self,l,r):
        Left,Right=self.__get_range(l,r)
        res=self.__e
        for i in Left+Right[::-1]:
            self.__propagate(i)
            res=self.__dot(res,self.__node[i])
        return res

# RmQ and range add
INF=float("inf")
A=[4,9,11,5,13,33,33,33,11,45,14,19,19,8,10,89]
from operator import add
tree=SegmentTree(A,min,INF,add,0,add)
print(tree._SegmentTree__get_range(4,12))
tree.add(2,8,4)
print(tree.sum(1,5))
print(tree.bisect(3,13,9.5,increase=False))

# segment tree (without lazy-propagation)
# cf. https://github.com/onakasuitacity/atcoder_py/blob/master/0_algorithm/lazy_propagation_segment_tree.py
class SegmentTree(object):
    def __init__(self,A,dot,e):
        n=2**((len(A)-1).bit_length())
        self.__n=n
        self.__dot=dot
        self.__e=e
        self.__node=[e]*(2*n-1)
        for i in range(len(A)):
            self.__node[n-1+i]=A[i]
        for i in range(n-2,-1,-1):
            self.__node[i]=dot(self.__node[2*i+1],self.__node[2*i+2])

    def update(self,i,c):
        i+=self.__n-1
        node=self.__node
        node[i]=c
        while(i!=0):
            i=(i-1)//2
            node[i]=self.__dot(node[2*i+1],node[2*i+2])

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

    def sum(self,l,r):
        Left,Right=self.__get_range(l,r)
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

#%% Example
from operator import add
A=[5,3,7,9,6,4,1,2]
N=len(A)
tree=SegmentTree(A,add,0)
print(tree._SegmentTree__node) # [37,24,13,8,16,10,3,5,3,7,9,6,4,1,2]

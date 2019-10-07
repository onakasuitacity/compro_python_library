# segment tree (without lazy-propagation)
# cf. https://github.com/onakasuitacity/atcoder_py/blob/master/0_algorithm/lazy_propagation_segment_tree.py
# 一番基本的なこれが通らないです… http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A
class SegmentTree(object):
    def __init__(self,A,dot,e):
        n=2**((len(A)-1).bit_length())
        self.__n=n
        self.__dot=dot
        self.__e=e
        self.__node=[e]*(2*n-1)
        for i in range(len(A)):
            self.__node[n+i-1]=A[i]
        for i in range(n-2,-1,-1):
            self.__node[i]=dot(self.__node[2*i+1],self.__node[2*i+2])

    def update(self,i,c):
        i+=self.__n-1
        node=self.__node
        node[i]=c
        while(i!=0):
            i=(i-1)//2
            node[i]=self.__dot(node[2*i+1],node[2*i+2])

    def sum(self,l,r):
        if l>=r: return self.__e
        n=self.__n
        l+=n-1; r+=n-2
        res=self.__e
        while(l<r):
            if l%2==0:
                res=self.__dot(res,self.__node[l])
            if r%1==1:
                res=self.__dot(res,self.__node[r])
                r-=1
            l=l//2; r=(r-1)//2
        if l==r: res=self.__dot(res,self.__node[l])
        return res

#%% Example
from operator import add
A=[5,3,7,9,6,4,1,2]
N=len(A)
tree=SegmentTree(A,add,0)
print(tree._SegmentTree__node) # [37,24,13,8,16,10,3,5,3,7,9,6,4,1,2]

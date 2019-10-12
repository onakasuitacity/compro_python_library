# segment tree (without lazy-propagation)
# cf. https://github.com/onakasuitacity/atcoder_py/blob/master/0_algorithm/lazy_propagation_segment_tree.py
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
        if(b==-1): b=self.__n
        if(increase):
            if(self.__node[i]<=x or b<=l or r<=a): return -1
            if(i>=self.__n): return i-self.__n
            lv=self.bisect(l,r,x,increase,2*i,a,(a+b)//2)
            if(lv!=-1): return lv
            return self.bisect(l,r,x,increase,2*i+1,(a+b)//2,b)
        else:
            if(self.__node[i]>=x or b<=l or r<=a): return -1
            if(i>=self.__n): return i-self.__n
            rv=self.bisect(l,r,x,increase,2*i+1,(a+b)//2,b)
            if(rv!=-1): return rv
            return self.bisect(l,r,x,increase,2*i,a,(a+b)//2)

# example
A=[4,9,11,5,13,33,33,33,11,45,14,19,19,8,10,89]
dot=min
e=float("inf")
tree=SegmentTree(A,dot,e)
print(tree.bisect(3,13,12,increase=False))

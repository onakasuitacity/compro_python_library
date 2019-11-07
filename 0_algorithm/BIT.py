# binary indexed tree (O(N),O(logN))
# http://hos.ac/slides/20140319_bit.pdf
class BIT(object):
    def __init__(self,A,dot,e,inv=None):
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
        i+=1
        res=self.__e
        while(i>0):
            res=self.__dot(res,self.__node[i])
            i-=i&-i
        return res

    def range_sum(self,l,r):
        assert(self.__inv)
        return self.__inv(self.sum(r),self.sum(l))

    def bisect_left(self,w,increase=True):
        if(w>self.sum(self.__n-1)): return self.__n
        n=2**((self.__n-1).bit_length())
        res=0
        while(n>0):
            if(res+n<=self.__n and ((w>self.__node[res+n])^(not increase))):
                w-=self.__node[res+n]
                res+=n
            n//=2
        return res

# example
from operator import add,sub
A=[5,3,7,9,6,4,1,2]
N=len(A)
bit=BIT(A,add,0,sub)
print(bit._BIT__node) # ['$',5,8,7,24,6,10,1,37]
print([bit.sum(i) for i in range(N)]) # [5,8,15,24,30,34,35,37]
print(bit.range_sum(3,5)) # 15=sum(A[3:5])
k=36
print(bit.bisect_left(k)) # 4

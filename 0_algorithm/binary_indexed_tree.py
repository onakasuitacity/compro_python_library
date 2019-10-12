# binary indexed tree (O(N),O(logN))
# http://hos.ac/slides/20140319_bit.pdf
class BIT(object):
    from operator import add
    def __init__(self,A,f=add):
        N=len(A)
        self.__len=N
        self.__f=f
        self.__node=A[:]
        for i in range(N):
            j=i+((i+1)&-(i+1))
            if(j<N): self.__node[j]=self.__f(self.__node[i],self.__node[j])

    def add(self,i,w):
        while(i<self.__len):
            self.__node[i]=self.__f(self.__node[i],w)
            i+=(i+1)&-(i+1)

    def sum(self,i):
        res=0
        while(i>-1):
            res=self.__f(res,self.__node[i])
            i-=(i+1)&-(i+1)
        return res

    def bisect_left(self,w):
        if w>self.sum(self.__len-1): return self.__len
        elif self.__len==1: return 0
        n=2**((self.__len-1).bit_length()-1)
        res=0
        while(n):
            if res+n-1>self.__len-1:
                n//=2
                continue
            if w<=self.__node[res+n-1]:
                n//=2
            else:
                w-=self.__node[res+n-1]
                res+=n
                n//=2
        return res


# Example
# https://slideshare.net/hcpc_hokudai/binary-indexed-tree
A=[5,3,7,9,6,4,1,2] # given sequence
N=len(A)
bit=BIT(A)
print(bit._BIT__node) # [5, 8, 7, 24, 6, 10, 1, 37]
print([bit.sum(i) for i in range(N)]) # [5, 8, 15, 24, 30, 34, 35, 37]

#%% cumsumのbinary search (O(logN))
k=30
print(bit.bisect_left(k)) # 4

#%% Query: A[0],...,A[k-1]にwを足す (O(logN))
k=3 # 3つ足す
w=2 # 計k*w足す
bit.add(k-1,k*w)
d_bit=BIT([0]*N)
d_bit.add(0,w)
d_bit.add(k-1,-w)
print([bit.sum(i)+(i+1)*d_bit.sum(i) for i in range(N)]) # [7, 12, 21, 30, 36, 40, 41, 43]

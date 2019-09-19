#%% Sparse Table O(NlogN)
# http://tookunn.hatenablog.com/entry/2016/07/13/211148

class SparseTable(object):
    """
    construct: O(NlogN)
    query: O(1)
    """
    def __init__(self,A):
        """
        A: list of float
        """
        # initialize
        self.__A=A[:]
        self.__n=len(A)
        self.__logn=max(0,(self.__n-1).bit_length())
        self.__maxtable=[[0]*self.__n for _ in range(self.__logn)]
        self.__maxtable[0]=list(range(self.__n))
        self.__mintable=[[0]*self.__n for _ in range(self.__logn)]
        self.__mintable[0]=list(range(self.__n))
        # construct(DP)
        for i in range(1,self.__logn):
            for k in range(self.__n):
                # [k:k+1<<(i-1)]と[k+(1<<(i-1)):k+(1<<i)]とに分けることで、i-1の結果を使える
                # k+(1<<(i-1))がindexを超えてるならば、前回の値がそのまま使える
                if k+(1<<(i-1))>=self.__n:
                    self.__maxtable[i][k]=self.__maxtable[i-1][k]
                    self.__mintable[i][k]=self.__mintable[i-1][k]
                    continue
                # そうでないときは、2つの区間に分けたときのAの大きさで判断
                # max
                if self.__A[self.__maxtable[i-1][k]]>=self.__A[self.__maxtable[i-1][k+(1<<(i-1))]]:
                    self.__maxtable[i][k]=self.__maxtable[i-1][k]
                else:
                    self.__maxtable[i][k]=self.__maxtable[i-1][k+(1<<(i-1))]
                # min
                if self.__A[self.__mintable[i-1][k]]<=self.__A[self.__mintable[i-1][k+(1<<(i-1))]]:
                    self.__mintable[i][k]=self.__mintable[i-1][k]
                else:
                    self.__mintable[i][k]=self.__mintable[i-1][k+(1<<(i-1))]
        
    def max(self,l,r):
        """
        param 0<=l<r<=n-1
        return i such that A[i]=max(A[l:r])
        """
        if r-l<=0: raise ValueError("l<r")
        if r-l==1: return l
        i=(r-l-1).bit_length()-1 # r-l>=2
        if self.__A[self.__maxtable[i][l]]>=self.__A[self.__maxtable[i][r-(1<<i)]]:
            return self.__maxtable[i][l]
        else:
            return self.__maxtable[i][r-(1<<i)]

    def min(self,l,r):
        """
        param 0<=l<r<=n-1
        return i such that A[i]=min(A[l:r])
        """
        if r-l<=0: raise ValueError("l<r")
        if r-l==1: return l
        i=(r-l-1).bit_length()-1 # r-l>=2
        if self.__A[self.__mintable[i][l]]<=self.__A[self.__mintable[i][r-(1<<i)]]:
            return self.__mintable[i][l]
        else:
            return self.__mintable[i][r-(1<<i)]
        
#%% input
A=[2,5,3,9,8,2,10,1,7,2,1,6]
table=SparseTable(A)
n=len(A)
from itertools import product
for l,r in product(range(n),repeat=2):
    if r-l<=0: continue 
    print(l,r,table.max(l,r),table.min(l,r))
print(table.max(l,r))
print(table.min(l,r))

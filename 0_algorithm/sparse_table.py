#%% Sparse Table O(NlogN)
# http://tookunn.hatenablog.com/entry/2016/07/13/211148
class SparseTable(object):
    """
    construct: O(NlogN)
    query:
        max: O(1)
        min: O(1)
    """
    def __init__(self,A):
        """
        A: list of float
        """
        # initialize
        n=len(A)
        logn=max(0,(n-1).bit_length())
        maxtable=[[0]*n for _ in range(logn)]
        maxtable[0]=A[:]
        mintable=[[0]*n for _ in range(logn)]
        mintable[0]=A[:]
        # construct
        from itertools import product
        for i,k in product(range(1,logn),range(n)):
            # [k:k+1<<(i-1)]と[k+(1<<(i-1)):k+(1<<i)]とに分けることで、i-1の結果を使える
            # k+(1<<(i-1))がindexを超えてるならば、前回の値がそのまま使える
            if k+(1<<(i-1))>=n:
                maxtable[i][k]=maxtable[i-1][k]
                mintable[i][k]=mintable[i-1][k]
            # そうでないときは、2つの区間に分けたときの大きさで判断
            else:
                maxtable[i][k]=max(maxtable[i-1][k],maxtable[i-1][k+(1<<(i-1))])
                mintable[i][k]=min(mintable[i-1][k],mintable[i-1][k+(1<<(i-1))])
        self.__n=n
        self.__maxtable=maxtable
        self.__mintable=mintable

    def max(self,l,r):
        """
        l,r: int 0<=l<r<=n
        return max(A[l:r])
        """
        n=self.__n
        assert 0<=l<r<=n
        i=max(0,(r-l-1).bit_length()-1)
        maxtable=self.__maxtable
        return max(maxtable[i][l],maxtable[i][r-(1<<i)])

    def min(self,l,r):
        """
        l,r: int 0<=l<r<=n
        return min(A[l:r])
        """
        n=self.__n
        assert 0<=l<r<=n
        i=max(0,(r-l-1).bit_length()-1)
        mintable=self.__mintable
        return min(mintable[i][l],mintable[i][r-(1<<i)])

#%% example
A=[2,5,3,9,8,2,10,1,7,2,1,6]
table=SparseTable(A)
n=len(A)
from itertools import product
for l,r in product(range(n),range(1,n+1)):
    if r-l<=0: continue
    print(l,r,table.max(l,r),table.min(l,r))

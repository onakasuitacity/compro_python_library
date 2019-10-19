# 2-dim cumulative sum
class cumsum_2D(object):
    def __init__(self,A):
        "A: 2-dim matrix"
        S=[a[:] for a in A] # deep copy
        from itertools import product
        for i,j in product(range(len(A)),range(len(A[0]))):
            if(i): S[i][j]+=S[i-1][j]
            if(j): S[i][j]+=S[i][j-1]
            if(i and j): S[i][j]-=S[i-1][j-1]
        self.__S=S

    @property
    def cumsum(self):
        return self.__S
        
    def sum(self,l1,r1,l2,r2):
        if(l1>=r1 or l2>=r2): return 0
        S=self.__S
        res=S[r1-1][r2-1]
        if(l1): res-=S[l1-1][r2-1]
        if(l2): res-=S[r1-1][l2-1]
        if(l1 and l2): res+=S[l1-1][l2-1]
        return res

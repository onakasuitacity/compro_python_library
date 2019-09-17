# Union Find (with Path compression)
# https://www.slideshare.net/chokudai/union-find-49066733
class UnionFind(object):
    """
    query: O(Ack^-1(n,n)) (amortize)
    """
    def __init__(self,n):
        """
        param n: number of nodes
        """
        self.__par=list(range(n))
        self.__rank=[0]*n

    def __root(self,k):
        if self.__par[k]==k: return k
        else:
            self.__par[k]=self.__root(self.__par[k])
            return self.__par[k]

    def same(self,i,j):
        return self.__root(i)==self.__root(j)

    def unite(self,i,j):
        i=self.__root(i)
        j=self.__root(j)
        if i==j: return
        if self.__rank[i]>self.__rank[j]: # rankが大きいほうが親になる
            self.__par[j]=i
        elif self.__rank[i]<self.__rank[j]:
            self.__par[j]=i
        else: # rankが同じときはどっちでもよい
            self.__par[j]=i
            self.__rank[i]+=1

#%%
union=UnionFind(6)
union.unite(0,2)
union.unite(1,3)
union.unite(1,5)
print(union.same(3,5))
print(union.same(2,4))

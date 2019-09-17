# Union Find (with Path compression)
# https://www.slideshare.net/chokudai/union-find-49066733
class UnionFind(object):
    """
    query: O(logN) (amortize)
    """
    def __init__(self,n):
        """
        param n: number of nodes
        """
        self.__par=list(range(n))

    def __get_root(self,k):
        if self.__par[k]==k: return k
        else:
            self.__par[k]=self.__get_root(self.__par[k])
            return self.__par[k]

    def same(self,i,j):
        return self.__get_root(i)==self.__get_root(j)

    def unite(self,i,j):
        i=self.__get_root(i)
        j=self.__get_root(j)
        if i==j: return
        self.__par[i]=j

#%%
union=UnionFind(6)
union.unite(0,2)
union.unite(1,3)
union.unite(1,5)
print(union.same(3,5))
print(union.same(2,4))

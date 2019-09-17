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
        self.__size=[1]*n

    def __root(self,k):
        if self.__par[k]==k: return k
        else:
            self.__par[k]=self.__root(self.__par[k])
            return self.__par[k]

    def is_same(self,i,j):
        return self.__root(i)==self.__root(j)

    def unite(self,i,j):
        i=self.__root(i)
        j=self.__root(j)
        if i==j: return
        if self.__rank[i]>self.__rank[j]:
            self.__par[j]=i
            self.__size[i]+=self.__size[j]
        else:
            self.__par[i]=j
            self.__size[j]+=self.__size[i]
            if self.__rank[i]==self.__rank[j]: self.__rank[j]+=1

    def size(self,k):
        return self.__size[self.__root(k)]

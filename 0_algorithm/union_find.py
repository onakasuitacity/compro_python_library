# Union Find (amortized O(ack^-1(N)))
# https://www.slideshare.net/chokudai/union-find-49066733
class UnionFind(object):
    def __init__(self,n):
        self.__par=list(range(n))
        self.__rank=[0]*n
        self.__size=[1]*n

    def root(self,k):
        if(self.__par[k]==k): return k
        self.__par[k]=self.root(self.__par[k])
        return self.__par[k]

    def unite(self,i,j):
        i=self.root(i); j=self.root(j)
        par=self.__par; rank=self.__rank; size=self.__size
        if(i==j): return False
        if(rank[i]>rank[j]):
            par[j]=i
            size[i]+=size[j]
        else:
            par[i]=j
            size[j]+=size[i]
            if(rank[i]==rank[j]): rank[j]+=1
        return True

    def is_same(self,i,j):
        return self.root(i)==self.root(j)

    def size(self,k):
        return self.__size[self.root(k)]

# example
tree=UnionFind(6)
tree.unite(0,2)
tree.unite(1,3)
tree.unite(1,5)
print(tree.size(3)) # 3

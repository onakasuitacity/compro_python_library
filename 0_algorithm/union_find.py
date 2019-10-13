# Union Find (amortized O(ack^-1(N)))
# https://www.slideshare.net/chokudai/union-find-49066733
class UnionFind(object):
    from operator import add
    def __init__(self,n,size=None,add=add):
        self.__par=list(range(n))
        self.__rank=[0]*n
        self.__size=size if size else [1]*n
        self.__add=add

    def root(self,k):
        if(self.__par[k]==k): return k
        self.__par[k]=self.root(self.__par[k])
        return self.__par[k]

    def unite(self,i,j):
        i=self.root(i); j=self.root(j)
        par=self.__par; rank=self.__rank; size=self.__size
        if(i==j): return
        if(rank[i]>rank[j]):
            par[j]=i
            size[i]=self.__add(size[i],size[j])
        else:
            par[i]=j
            size[j]=self.__add(size[i],size[j])
            if(rank[i]==rank[j]): rank[j]+=1

    def size(self,k):
        return self.__size[self.root(k)]

# example
tree=UnionFind(6)
tree.unite(0,2)
tree.unite(1,3)
tree.unite(1,5)
print(tree.size(3)) # 3

# Union Find (amortized O(ack^-1(N)))
# https://www.slideshare.net/chokudai/union-find-49066733
class UnionFind(object):
    def __init__(self,n):
        self.__par=list(range(n))
        self.__size=[1]*n

    def root(self,i):
        p=i; par=self.__par
        while(p!=par[p]): p=par[p]
        while(i!=p): i,par[i]=par[i],p
        return p

    def unite(self,i,j):
        i=self.root(i); j=self.root(j)
        if(i==j): return False
        par=self.__par; size=self.__size
        if(size[i]<size[j]): i,j=j,i
        par[j]=i
        size[i]+=size[j]
        return True

    def is_same(self,i,j):
        return self.root(i)==self.root(j)

    def size(self,i):
        return self.__size[self.root(i)]

# example
tree=UnionFind(6)
tree.unite(0,2)
tree.unite(1,3)
tree.unite(1,5)
print(tree.size(3)) # 3

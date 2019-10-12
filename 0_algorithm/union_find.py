# Union Find (amortized O(ack^-1(N)))
# https://www.slideshare.net/chokudai/union-find-49066733
class UnionFind(object):
    def __init__(self,n):
        self.__par=list(range(n))
        self.__rank=[0]*n
        self.__size=[1]*n

    def __root(self,k):
        if(self.__par[k]==k): return k
        else:
            self.__par[k]=self.__root(self.__par[k])
            return self.__par[k]

    def is_same(self,i,j):
        return self.__root(i)==self.__root(j)

    def unite(self,i,j):
        i=self.__root(i)
        j=self.__root(j)
        if(i==j): return
        if(self.__rank[i]>self.__rank[j]):
            self.__par[j]=i
            self.__size[i]+=self.__size[j]
        else:
            self.__par[i]=j
            self.__size[j]+=self.__size[i]
            if(self.__rank[i]==self.__rank[j]): self.__rank[j]+=1

    def size(self,k):
        return self.__size[self.__root(k)]

# example
tree=UnionFind(6)
tree.unite(0,2)
tree.unite(1,3)
tree.unite(1,5)
print(tree.is_same(3,5)) # True
print(tree.is_same(2,4)) # False
print(tree.size(3)) # 3

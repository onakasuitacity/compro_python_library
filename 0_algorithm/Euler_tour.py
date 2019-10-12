# Euler tour (O(V))
# https://www.npca.jp/works/magazine/2015_5/
class EulerTour(object):
    def __init__(self,E,root=0):
        """
        E: adjacency list
        """
        n=len(E)
        self.__V=list(range(n))
        self.__E=E 
        self.__begin=[0]*n
        self.__end=[0]*n
        self.__tour=[0]*(2*n-1)
        self.__k=0
        self.__dfs(root,-1)
        del self.__k

    def __dfs(self,v,p):
        self.__begin[v]=self.__k
        self.__tour[self.__k]=v
        self.__k+=1
        for u in self.__E[v]:
            if(u==p): continue
            self.__dfs(u,v)
            self.__tour[self.__k]=v
            self.__k+=1
        self.__end[v]=self.__k

    @property
    def begin(self):
        return self.__begin

    @property
    def end(self):
        return self.__end

    @property
    def tour(self):
        return self.__tour

# example
N=6
V=list(range(N))
E=[[1,2],[0],[0,3,4,5],[2],[2],[2]]

###
#    0
#   / \
#  1   2
#     /|\
#    3 4 5

tree=EulerTour(E)
print(tree.tour) # [0,1,0,2,3,2,4,2,5,2,0]
print(tree.begin) # [0,1,3,4,6,8]
print(tree.end) # [11,2,10,5,7,9]

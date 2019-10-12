# LCA with doubling (O(NlogN),O(logN))
# https://tjkendev.github.io/procon-library/python/graph/lca-doubling.html
class LCA(object):
    def __init__(self,E,root=0):
        """
        E: adjacency list
        """
        self.__n=len(E)
        self.__E=E
        self.__logn=(self.__n-1).bit_length()
        self.__depth=[-1]*self.__n
        self.__depth[root]=0
        self.__parents=[[-1]*self.__n for _ in range(self.__logn)]
        self.__dfs(root)
        self.__doubling()

    def __dfs(self,v):
        for u in self.__E[v]:
            if(self.__depth[u]!=-1): continue
            self.__parents[0][u]=v
            self.__depth[u]=self.__depth[v]+1
            self.__dfs(u)

    def __doubling(self):
        for i in range(1,self.__logn):
            for v in range(self.__n):
                if(self.__parents[i-1][v]==-1): continue
                self.__parents[i][v]=self.__parents[i-1][self.__parents[i-1][v]]
    
    @property
    def depth(self):
        return self.__depth

    def get(self,u,v):
        dd=self.__depth[v]-self.__depth[u]
        if(dd<0): # vの方が深いようにする
            u,v=v,u
            dd*=-1
        for i in range(self.__logn):
            if(dd&(1<<i)): v=self.__parents[i][v]
        if(v==u): return v
        for i in range(self.__logn-1,-1,-1):
            pu,pv=self.__parents[i][u],self.__parents[i][v]
            if(pu!=pv): u,v=pu,pv
        return self.__parents[0][u]

# example
N=6
V=list(range(N))
E=[{1,2},{0},{0,3,4,5},{2},{3},{4}]

###
#    0
#   / \
#  1   2
#     /|\
#    3 4 5

a=LCA(E,0)
a.get(3,4) 

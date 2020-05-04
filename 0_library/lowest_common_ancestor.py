# LCA with doubling (O(NlogN),O(logN))
# https://tjkendev.github.io/procon-library/python/graph/lca-doubling.html
class LCA(object):
    def __init__(self,E,root=0):
        self.__n=len(E); self.__E=E; self.__logn=(self.__n-1).bit_length()
        self.__depth=[-1]*self.__n; self.__depth[root]=0
        self.__parent=[[-1]*self.__n for _ in range(self.__logn)]
        self.__dfs(root); self.__doubling()

    def __dfs(self,v):
        Q=[v]
        while(Q):
            v=Q.pop()
            for nv in self.__E[v]:
                if(self.__depth[nv]!=-1): continue
                self.__parent[0][nv]=v
                self.__depth[nv]=self.__depth[v]+1
                Q.append(nv)

    def __doubling(self):
        for k in range(1,self.__logn):
            for v in range(self.__n):
                if(self.__parent[k-1][v]==-1): continue
                self.__parent[k][v]=self.__parent[k-1][self.__parent[k-1][v]]

    def depth(self,v):
        return self.__depth[v]

    def kth_parent(self,k,v):
        return self.__parent[k][v]

    def dist(self,u,v):
        return self.__depth[u]+self.__depth[v]-2*self.__depth[self.get(u,v)]

    def get(self,u,v):
        dd=self.__depth[v]-self.__depth[u]
        if(dd<0):
            u,v=v,u
            dd*=-1
        for k in range(self.__logn):
            if((dd>>k)&1): v=self.__parent[k][v]
        if(v==u): return v
        for k in range(self.__logn-1,-1,-1):
            pu,pv=self.__parent[k][u],self.__parent[k][v]
            if(pu!=pv): u,v=pu,pv
        return self.__parent[0][u]

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

# Lowlink (O(V+E))
# https://www.npca.jp/works/magazine/2014_1/
# http://kagamiz.hatenablog.com/entry/2013/10/05/005213
class Lowlink(object):
    def __init__(self,E,root=0):
        """
        E: adjacency list
        """
        self.__n=len(E)
        self.__E=E
        self.__count=0
        self.__ord=[-1]*self.__n
        self.__low=[-1]*self.__n
        self.__bridge=[]
        self.__articulation=[]
        self.__dfs(root,-1)

    def __dfs(self,v,p): # p:parent
        ord=self.__ord
        low=self.__low
        ord[v]=self.__count
        low[v]=self.__count
        self.__count+=1
        isArticulation=False
        count=0 # DFS treeの子の数(rootのarticulate判定に必要)
        for u in self.__E[v]:
            if(ord[u]==-1): # まだ見てない
                count+=1
                self.__dfs(u,v)
                low[v]=min(low[v],low[u])
                if(ord[v]<low[u]): self.__bridge.append([min(u,v),max(u,v)])
                if(p!=-1 and ord[v]<=low[u]): isArticulation=True
            elif u!=p: # uは見たけどvuは通ってない(=後退辺(backward edge))
                low[v]=min(low[v],low[u])
        if(p==-1 and count>=2): isArticulation=True
        if(isArticulation): self.__articulation.append(v)

    @property
    def bridge(self):
        return self.__bridge

    @property
    def articulation(self):
        return self.__articulation

# example
E=[[4,1],[0,2],[4,3,1],[2],[0,6,2,7],[7],[4,7],[4,6,8,5],[7]]
low=Lowlink(E)
print(low.bridge)
print(low.articulation)

# Dijkstra's algorithm with heap tree O(ElogV)
# https://takeg.hatenadiary.jp/entry/2019/06/03/130418

class Dijkstra(object):
    """
    construct: O(ElogV)
    """
    
    def __init__(self,edges,start=0):
        """
        :param list of list of list of int edges:
        :param int start=0:
        """
        self.__dist=[float("inf")]*len(edges)
        self.__dist[start]=0
        self.__calculate(edges,start)

    @property
    def dist(self):
        return self.__dist
    
    def __calculate(self,edges,start):
        import heapq
        Q=[(0,start)] # (dist,vertex)
        while(Q):
            dist,v=heapq.heappop(Q)
            if self.dist[v]<dist: continue # 候補として挙がったd,vだが、他に短いのがある
            for u,cost in edges[v]:
                if self.dist[u]>self.dist[v]+cost:
                    self.__dist[u]=self.dist[v]+cost
                    heapq.heappush(Q,(self.dist[u],u))

# input
V=list(range(5))
E=[
[[1,50],[2,80]],
[[2,20],[3,15]],
[[3,10],[4,15]],
[[4,30]],
[]
]
dij=Dijkstra(E,0)
print(dij.dist) # [0,50,70,65,85]

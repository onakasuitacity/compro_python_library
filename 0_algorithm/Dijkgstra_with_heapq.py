# Dijkstra's algorithm with heap tree (O(ElogV))
# https://takeg.hatenadiary.jp/entry/2019/06/03/130418
class Dijkstra(object):
    def __init__(self,E,start=0):
        """
        E: adjacency list with weight
        """
        self.__dist=[float("inf")]*len(E)
        self.__dist[start]=0
        self.__calculate(E,start)

    @property
    def dist(self):
        return self.__dist
    
    def __calculate(self,E,start):
        import heapq
        dist=self.__dist
        Q=[(0,start)] # (dist,node)
        while(Q):
            d,v=heapq.heappop(Q)
            if dist[v]<d: continue # 候補として挙がったd,vだが、他に短いのがある
            for u,w in E[v]:
                if dist[u]>dist[v]+w:
                    dist[u]=dist[v]+w
                    heapq.heappush(Q,(dist[u],u))

# example
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

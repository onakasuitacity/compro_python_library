# Dijkstra's algorithm O(V^2)
# https://qiita.com/shizuma/items/e08a76ab26073b21c207

class Dijkstra(object):
    """
    construct: O(V^2)
    """
    
    def __init__(self,edges,start=0):
        """
        :param list of list of list of int edges:
        :param int start=0:
        """
        self.__V=list(range(len(edges)))
        self.__dist=[float("inf")]*len(edges)
        self.__dist[start]=0
        self.__prev=[None]*len(edges)
        self.__calculate(edges,start)

    @property
    def dist(self):
        return self.__dist

    @property
    def prev(self):
        return self.__prev
    
    def __calculate(self,edges,start):
        Q=set(self.__V)
        while(Q):
            # Qの中で距離が最小のものを取得
            v = min((self.dist[v],v) for v in Q)[1]
            Q.remove(v)
            # iの出力辺の先を探索
            for u,cost in edges[v]:
                if self.dist[u]>self.dist[v]+cost:
                    self.__dist[u]=self.dist[v]+cost
                    self.__prev[u]=v
                    
# input
V=list(range(5))
E=[
[[1,50],[2,80]],
[[2,20],[3,15]],
[[3,10],[4,15]],
[[4,30]],
[]
]
start=0

# output
dij=Dijkstra(E,start)
for i in V:
    print("FROM {} TO {}".format(s,i))
    print("distance : {}".format(dij.dist[i]))
    p=i
    path=[i]
    while(dij.prev[p]):
        p=dij.prev[p]
        path.append(p)
    print("path : {}".format(path[::-1]),end="\n\n")

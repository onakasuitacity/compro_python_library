# Dijkstra's algorithm O(V^2)
# https://qiita.com/shizuma/items/e08a76ab26073b21c207
class Dijkstra(object):    
    def __init__(self,E,start=0):
        """
        E: adjacency list with weight
        """
        self.__V=list(range(len(E)))
        self.__dist=[float("inf")]*len(E)
        self.__dist[start]=0
        self.__prev=[None]*len(E)
        self.__calculate(E,start)

    @property
    def dist(self):
        return self.__dist

    @property
    def prev(self):
        return self.__prev
    
    def __calculate(self,E,start):
        dist=self.__dist
        Q=set(self.__V)
        while(Q):
            # Qの中で距離が最小のものを取得
            v=min((self.dist[v],v) for v in Q)[1]
            Q.remove(v)
            # iの出力辺の先を探索
            for u,w in E[v]:
                if dist[u]>dist[v]+w:
                    dist[u]=dist[v]+w
                    self.__prev[u]=v
                    
# example
V=list(range(5))
E=[
[[1,50],[2,80]],
[[2,20],[3,15]],
[[3,10],[4,15]],
[[4,30]],
[]
]
start=0

dij=Dijkstra(E,start)
for i in V:
    print("FROM {} TO {}".format(start,i))
    print("distance : {}".format(dij.dist[i]))
    p=i
    path=[i]
    while(dij.prev[p]):
        p=dij.prev[p]
        path.append(p)
    print("path : {}".format(path[::-1]),end="\n\n")

#%% Bellman-Ford algorithm O(VE)
# http://wakabame.hatenablog.com/entry/2017/09/06/221400

class BellmanFord(object):
    """
    construct: O(VE)
    """

    def __init__(self,edges,start=0):
        """
        :param list of list of [node,cost] edges:
        :param int start=0:
        """
        self.__n=len(edges)
        self.__dist=[float("inf")]*self.__n
        self.__dist[start]=0
        self.__calculate(edges,start)

    @property
    def dist(self):
        return self.__dist

    def __calculate(self,edges,start): # relaxingという
        for k in range(self.__n): # n回更新する。n回目に更新が行われたら負経路あり。
            update=False
            for v in range(self.__n):
                for u,cost in edges[v]:
                    if self.dist[u]>self.dist[v]+cost:
                        self.__dist[u]=self.dist[v]+cost
                        update=True
            else:
                if (update is False): # 更新されない＝終わり
                    return
                elif (update is True) and (k==self.__n-1): # 負の閉路検出
                    self.__dist=[-float("inf")]*self.__n

# input
V=list(range(5))
E=[
[[1,50],[2,80]],
[[2,20],[3,15]],
[[3,10],[4,15]],
[[4,30]],
[]
]
bel=BellmanFord(E,0)
print(bel.dist) # [0,50,70,65,85]

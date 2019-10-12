# Bellman-Ford algorithm (O(VE))
# http://wakabame.hatenablog.com/entry/2017/09/06/221400
class BellmanFord(object):
    def __init__(self,E,start=0):
        """
        E: adjacency list with weight
        """
        self.__n=len(E)
        self.__dist=[float("inf")]*self.__n
        self.__dist[start]=0
        self.__calculate(E,start)

    @property
    def dist(self):
        return self.__dist

    def __calculate(self,E,start): # relaxingという
        dist=self.__dist
        for k in range(self.__n): # n回更新する。n回目に更新が行われたら負経路あり。
            update=False
            for v in range(self.__n):
                for u,w in E[v]:
                    if dist[u]>dist[v]+w:
                        dist[u]=dist[v]+w
                        update=True
            if (update is False): # 更新されない＝終わり
                return
            elif (update is True) and (k==self.__n-1): # 負の閉路検出
                self.__dist=[-float("inf")]*self.__n

# example
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

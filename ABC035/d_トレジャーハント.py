# https://atcoder.jp/contests/abc035/submissions/7493216
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
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
    n,m,t=map(int,input().split())
    E=[[] for _ in range(n)]
    revE=[[] for _ in range(n)]
    A=list(map(int,input().split()))
    for _ in range(m):
        a,b,c=map(int,input().split())
        a-=1
        b-=1
        E[a].append([b,c])
        revE[b].append([a,c])
    dij=Dijkstra(E,0)
    revdij=Dijkstra(revE,0)
    print(max(A[i]*(t-dij.dist[i]-revdij.dist[i]) for i in range(n)))

resolve()

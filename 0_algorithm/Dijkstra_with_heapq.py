# Dijkstra with heap tree (O(ElogV))
# https://qiita.com/shizuma/items/e08a76ab26073b21c207
from heapq import heappop,heappush
INF=float("inf")
n=5
s=0
E=[
[(1,50),(2,80)],
[(2,20),(3,15)],
[(3,10),(4,15)],
[(4,30)],
[]
]

dist=[INF]*n
dist[s]=0
prev=[-1]*n
Q=[(0,s)] # (d,v)
while(Q):
    d,v=heappop(Q)
    if(dist[v]<d): continue
    for nv,w in E[v]:
        if(dist[nv]>dist[v]+w):
            dist[nv]=dist[v]+w
            prev[nv]=v
            heappush(Q,(dist[nv],nv))

print(dist)
print(prev)

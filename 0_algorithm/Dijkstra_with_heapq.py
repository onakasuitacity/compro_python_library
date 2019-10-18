# Dijkstra with heap tree (O(ElogV))
# https://qiita.com/shizuma/items/e08a76ab26073b21c207
INF=float("inf")
n=5
u=0
E=[
[(1,50),(2,80)],
[(2,20),(3,15)],
[(3,10),(4,15)],
[(4,30)],
[]
]
import heapq
Q=[(0,u)] # (d,v)
dist=[INF]*n
dist[u]=0
prev=[-1]*n
while(Q):
    d,v=heapq.heappop(Q)
    if(dist[v]<d): continue
    for nv,w in E[v]:
        if(dist[nv]>dist[v]+w):
            dist[nv]=dist[v]+w
            prev[nv]=v
            heapq.heappush(Q,(dist[nv],nv))

# path restoration (O(N))
v=4
path=[]
while(v!=-1):
    path.append(v)
    v=prev[v]
print(path[::-1])

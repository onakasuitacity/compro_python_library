# pure Dijkstra's algorithm (O(V^2))
# https://qiita.com/shizuma/items/e08a76ab26073b21c207
n=5
INF=float("inf")
u=0 # start (パラメータで持つ必要はなく、distを0で初期化するだけ)
E=[
[[1,50],[2,80]],
[[2,20],[3,15]],
[[3,10],[4,15]],
[[4,30]],
[]
]

dist=[INF]*n; dist[u]=0
prev=[-1]*n
calculated=[False]*n
for _ in range(n-1):
    v=min((dist[v],v) for v in range(n) if(not calculated[v]))[1]
    calculated[v]=True
    for nv,w in E[v]:
        if(dist[nv]>dist[v]+w):
            dist[nv]=dist[v]+w
            prev[nv]=v
print(dist) # [0,50,70,65,85]
print(prev) # [-1,0,1,1,2]

# Bellman-Ford algorithm (O(VE))
# http://wakabame.hatenablog.com/entry/2017/09/06/221400
INF=float("inf")
# example
n=5
V=list(range(n))
E=[
[[1,50],[2,80]],
[[2,20],[3,15]],
[[3,10],[4,15]],
[[4,30]],
[]
]
s=0
dist=[INF]*n
dist[s]=0

for k in range(n):
    update=False
    for v in range(n):
        for nv,w in E[v]:
            if(dist[nv]>dist[v]+w):
                dist[nv]=dist[v]+w
                update=True
    if(not update):
        break
    elif(k==n-1):
        print("Found negative loop")

print(dist) # [0,50,70,65,85]

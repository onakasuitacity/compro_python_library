# Dijkstra's algorithm with heap tree O(ElogV)
# https://takeg.hatenadiary.jp/entry/2019/06/03/130418

# constant
INF=float("inf")

# input
V=list(range(5))
E=[
[[1,50],[2,80]],
[[2,20],[3,15]],
[[3,10],[4,15]],
[[4,30]],
[]
]
n=len(V)
m=7 # 使わない

# start
s=0

# initialize
d=[INF]*n
d[s]=0

# iterate
import heapq
Q=[]
heapq.heapify(Q)
heapq.heappush(Q,(0,s)) # (cost,v)

while(Q):
    dist,v=heapq.heappop(Q)
    if d[v]<dist: continue # 候補として挙がったdist,vだが、他で短いのがある
    for i,cost in E[v]:
        if d[i]>d[v]+cost:
            d[i]=d[v]+cost
            heapq.heappush(Q,(d[i],i))

print(d) # [0,50,70,65,85]

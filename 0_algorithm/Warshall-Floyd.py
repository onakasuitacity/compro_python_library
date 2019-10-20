# Warshall-Floyd algorithm (O(N^3))
# https://qiita.com/shizuma/items/e08a76ab26073b21c207
INF=float("inf")
n=5
A=[
[INF, 50, 80,INF,INF],
[INF,INF, 20, 15,INF],
[INF,INF,INF, 10, 15],
[INF,INF,INF,INF, 30],
[INF,INF,INF,INF,INF]
]
next=[list(range(n)) for _ in range(n)]
from itertools import product
for k,i,j in product(range(n),repeat=3):
    if(A[i][j]>A[i][k]+A[k][j]):
        A[i][j]=A[i][k]+A[k][j]
        next[i][j]=next[i][k]

#  restoration
u=0; v=4
path=[u]
while(u!=v):
    u=next[u][v]
    path.append(u)
print(path) # [0,1,2,4]

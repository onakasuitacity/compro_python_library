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
B=[a[:] for a in A] # deep copy
from itertools import product
for k,i,j in product(range(n),repeat=3):
    B[i][j]=min(B[i][j],B[i][k]+B[k][j])

# route restoration (O(N^2))
u=0
v=4
path=[u]
while(B[u][v]!=A[u][v]):
    for w in range(n):
        if(B[u][v]==A[u][w]+B[w][v]):
            u=w
            path.append(w)
            break
path.append(v)
print(path) # [0,1,2,4]

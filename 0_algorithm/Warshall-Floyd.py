# Warshall–Floyd algorithm

### input
# node
V=[0,1,2,3,4]
n=len(V)
# adjacency matrix
inf=float("inf")
A = [
[0,50,80,inf,inf],
[inf,0,20,15,inf],
[inf,inf,0,10,15],
[inf,inf,inf,0,30],
[inf,inf,inf,inf,0]
]
m=7 #使わない

### algorithm
from itertools import product
for k,i,j in product(range(n),range(n),range(n)):
    A[i][j]=min(A[i][j],A[i][k]+A[k][j])

### output
print(*A,sep='\n')

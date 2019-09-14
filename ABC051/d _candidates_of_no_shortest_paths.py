# https://atcoder.jp/contests/abc051/tasks/abc051_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n,m=map(int,input().split())
    A=[[INF]*n for _ in range(n)]
    for i in range(n): A[i][i]=0
    for _ in range(m):
        a,b,c=map(int,input().split())
        a-=1
        b-=1
        A[a][b]=c
        A[b][a]=c
    from copy import deepcopy
    C=deepcopy(A)
    # Warshall-Floyd
    from itertools import product
    for k,i,j in product(range(n),repeat=3):
        A[i][j]=min(A[i][j],A[i][k]+A[k][j])
    # count
    B=set()
    for s,i,j in product(range(n),repeat=3):
        if (C[i][j]!=INF) and (i!=j) and (A[s][i]+C[i][j]==A[s][j]):
            B.add((min(i,j),max(i,j)))
    print(m-len(B))

resolve()

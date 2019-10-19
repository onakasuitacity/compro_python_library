# https://atcoder.jp/contests/abc143/tasks/abc143_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m,L=map(int,input().split())
    A=[[INF]*n for _ in range(n)]
    for _ in range(m):
        a,b,c=map(int,input().split())
        a-=1; b-=1
        A[a][b]=A[b][a]=c
    from itertools import product
    for k,i,j in product(range(n),repeat=3):
        A[i][j]=min(A[i][j],A[i][k]+A[k][j])
    B=[[INF]*n for _ in range(n)]
    for i,j in product(range(n),repeat=2):
        if(A[i][j]<=L): B[i][j]=1
    for k,i,j in product(range(n),repeat=3):
        B[i][j]=min(B[i][j],B[i][k]+B[k][j])
    Q=int(input())
    for _ in range(Q):
        s,t=map(int,input().split())
        s-=1; t-=1
        print(B[s][t]-1 if(B[s][t]!=INF) else -1)
resolve()

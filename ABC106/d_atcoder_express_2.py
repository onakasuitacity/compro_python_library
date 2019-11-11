# https://atcoder.jp/contests/abc106/tasks/abc106_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m,q=map(int,input().split())
    A=[[0]*n for _ in range(n)]
    for _ in range(m):
        l,r=map(int,input().split())
        l-=1; r-=1
        A[l][r]+=1
    S=[[0]*(n+1) for _ in range(n+1)]
    from itertools import product
    for i,j in product(range(n),repeat=2):
        S[i+1][j+1]=A[i][j]+S[i][j+1]+S[i+1][j]-S[i][j]
    for _ in range(q):
        l,r=map(int,input().split())
        print(S[r][r]-S[l-1][r]-S[r][l-1]+S[l-1][l-1])
resolve()

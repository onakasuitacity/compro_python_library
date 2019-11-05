# https://atcoder.jp/contests/abc130/tasks/abc130_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    S=list(map(int,input().split()))
    T=list(map(int,input().split()))
    C=[[0]*(m+1) for _ in range(n+1)]
    from itertools import product
    for i,j in product(range(n),range(m)):
        dp=C[i][j]+1 if(S[i]==T[j]) else 0
        C[i+1][j+1]=dp+C[i][j+1]+C[i+1][j]-C[i][j]
        C[i+1][j+1]%=MOD
    print(C[n][m]+1)
resolve()

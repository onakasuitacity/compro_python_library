# https://atcoder.jp/contests/abc122/tasks/abc122_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    N=int(input())
    dp=[[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    # initialize(n=3)
    NG={(0,1,2),(1,0,2),(0,2,1)}
    from itertools import product
    for i,j,k in product(range(4),repeat=3):
        if (i,j,k) in NG: continue
        dp[3][i][j][k]=1
    # iterate
    for n in range(4,N+1):
        for i,j,k,l in product(range(4),repeat=4):
            if dp[n-1][i][j][k]==0: continue
            if (j,k,l) in NG: continue
            if (i,j,l)==(0,1,2): continue
            if (i,k,l)==(0,1,2): continue
            dp[n][j][k][l]+=dp[n-1][i][j][k]
    # calculate
    ans=0
    for i,j,k in product(range(4),repeat=3):
        ans+=dp[N][i][j][k]
    print(ans%MOD)

resolve()

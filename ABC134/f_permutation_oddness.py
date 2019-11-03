# https://atcoder.jp/contests/abc134/tasks/abc134_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,K=map(int,input().split())
    dp=[[[0]*2700 for _ in range(55)] for _ in range(55)]
    dp[0][0][0]=1
    for i in range(n):
        for j in range(i+1):
            for k in range(K+1):
                dp[i+1][j][k+2*j]+=(2*j+1)*dp[i][j][k]
                dp[i+1][j][k+2*j]%=MOD
                dp[i+1][j+1][k+2*(j+1)]+=dp[i][j][k]
                dp[i+1][j+1][k+2*(j+1)]%=MOD
                if(j):
                    dp[i+1][j-1][k+2*(j-1)]+=j*j*dp[i][j][k]
                    dp[i+1][j-1][k+2*(j-1)]%=MOD
    print(dp[n][0][K])
resolve()

# https://atcoder.jp/contests/abc145/tasks/abc145_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    H=[0]+list(map(int,input().split()))

    dp=[[INF]*(n-k+1) for _ in range(n+1)]
    dp[0][0]=0

    for x in range(1,n+1):
        for y in range(1,n-k+1):
            dp[x][y]=min(dp[x0][y-1]+max(0,H[x]-H[x0]) for x0 in range(x))

    print(min(dp[x][n-k] for x in range(n+1)))
resolve()

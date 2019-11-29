# https://atcoder.jp/contests/abc044/tasks/arc060_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,a=map(int,input().split())
    X=list(map(int,input().split()))
    M=sum(X)
    dp=[[0]*(M+1) for _ in range(n+1)]
    dp[0][0]=1

    from itertools import product
    for x in X:
        ndp=[y[:] for y in dp]
        for i,m in product(range(n),range(M+1)):
            if(m+x<=M):
                ndp[i+1][m+x]+=dp[i][m]
        dp=ndp

    ans=0
    for i in range(1,n+1):
        if(i*a<=M):
            ans+=dp[i][i*a]
    print(ans)
resolve()

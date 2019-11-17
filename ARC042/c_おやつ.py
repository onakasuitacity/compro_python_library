# https://atcoder.jp/contests/arc042/tasks/arc042_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,P=map(int,input().split())
    AB=[tuple(map(int,input().split())) for _ in range(n)]
    AB.sort(reverse=1)

    ans=-INF
    dp=[0]*(P+1)
    for i in range(n):
        a,b=AB[i]
        ndp=dp[:]
        for p in range(P+1):
            if(p+a<=P):
                ndp[p+a]=max(ndp[p+a],dp[p]+b)
            else:
                ans=max(ans,dp[p]+b)
        dp=ndp
    print(ans)
resolve()

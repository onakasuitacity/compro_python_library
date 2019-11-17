# https://atcoder.jp/contests/abc145/tasks/abc145_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,T=map(int,input().split())
    AB=[tuple(map(int,input().split())) for _ in range(n)]
    AB.sort()

    dp=[0]*T
    ans=-INF
    for i in range(n):
        a,b=AB[i]
        ndp=dp[:]
        for t in range(T):
            if(t+a<T):
                ndp[t+a]=max(ndp[t+a],dp[t]+b)
            else:
                ans=max(ans,dp[t]+b)
        dp=ndp
    print(ans)
resolve()

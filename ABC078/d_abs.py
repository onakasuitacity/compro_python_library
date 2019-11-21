# https://atcoder.jp/contests/abc078/tasks/arc085_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,z,w=map(int,input().split()) # 必ず捨てられるため、zの値は関係ない
    A=[w]+list(map(int,input().split()))
    dp=[[None]*2 for _ in range(n+1)] # dp[i][turn] 消費枚数i,turnの手から始まるときの最適解

    def dfs(i,turn)->NoneType:
        if(dp[i][turn] is not None): return

        # i+1からn-1のdp[1-turn]を埋めておく(i=n-1のときterminate)
        for j in range(i+1,n):
            dfs(j,1-turn)

        res=-INF if(turn==0) else INF
        if(turn==0):
            for j in range(i+1,n):
                res=max(res,dp[j][1])
            res=max(res,abs(A[-1]-A[i]))
        else:
            for j in range(i+1,n):
                res=min(res,dp[j][0])
            res=min(res,abs(A[-1]-A[i]))
        dp[i][turn]=res

    dfs(0,0)
    print(dp[0][0])
resolve()

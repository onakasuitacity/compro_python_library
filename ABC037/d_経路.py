# https://atcoder.jp/contests/abc037/tasks/abc037_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    h,w=map(int,input().split())
    G=[list(map(int,input().split())) for _ in range(h)]

    dp=[[-1]*w for _ in range(h)]
    D=[(-1,0),(1,0),(0,-1),(0,1)]

    def dfs(i,j)->int:
        if(dp[i][j]!=-1): return dp[i][j]
        res=1
        for di,dj in D:
            if(0<=i+di<h and 0<=j+dj<w and G[i][j]<G[i+di][j+dj]):
                res+=dfs(i+di,j+dj)
                res%=MOD
        dp[i][j]=res
        return res

    ans=0
    for i in range(h):
        for j in range(w):
            ans+=dfs(i,j)
            ans%=MOD
    print(ans)
resolve()

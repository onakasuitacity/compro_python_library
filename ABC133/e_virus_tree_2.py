# https://atcoder.jp/contests/abc133/submissions/8282936
# PyPyだとTLE
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=map(int,input().split())
        a-=1; b-=1;
        E[a].append(b)
        E[b].append(a)

    dp=[1]*n
    dp[0]=k
    def dfs(v,p)->None:
        if(p!=-1):
            count=0
            for nv in E[v]:
                if(nv==p): continue
                dp[nv]=k-2-count
                count+=1
                dfs(nv,v)
        else:
            count=0
            for nv in E[v]:
                dp[nv]=k-1-count
                count+=1
                dfs(nv,v)

    dfs(0,-1)
    ans=1
    for i in range(n):
        ans*=dp[i]
        ans%=MOD
    print(ans)
resolve()

# https://atcoder.jp/contests/abc041/tasks/abc041_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    E=[0]*n
    for _ in range(m):
        x,y=map(lambda x:int(x)-1,input().split())
        E[x]+=(1<<y)
    dp=[0]*(1<<n)
    dp[0]=1
    # 配るDP
    for S in range(1<<n):
        for v in range(n):
            if not S&(1<<v):
                if not (S&E[v]):
                    dp[S+(1<<v)]+=dp[S]
    print(dp[(1<<n)-1])
resolve()

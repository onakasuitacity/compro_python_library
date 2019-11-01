# https://atcoder.jp/contests/dp/tasks/dp_u
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=[list(map(int,input().split())) for _ in range(n)]
    N=1<<n
    cost=[0]*N
    for mask in range(N):
        for j in range(n):
            for i in range(j):
                if((mask>>i)&1 and (mask>>j)&1):
                    cost[mask]+=A[i][j]
    dp=[-INF]*N
    dp[0]=0
    for mask in range(1,N):
        mask2=mask
        while(mask2):
            tmp=dp[mask&~mask2]+cost[mask2]
            dp[mask]=max(dp[mask],tmp)
            mask2=(mask2-1)&mask
    print(dp[-1])
resolve()

# https://atcoder.jp/contests/abc054/tasks/abc054_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from itertools import product
def resolve():
    n,ma,mb=map(int,input().split())
    ABC=[tuple(map(int,input().split())) for _ in range(n)]
    M=400

    dp=[[INF]*(M+1) for _ in range(M+1)]
    dp[0][0]=0

    for a,b,c in ABC:
        for x,y in product(range(M,-1,-1),repeat=2):
            if(x+a<=M and y+b<=M):
                dp[x+a][y+b]=min(dp[x+a][y+b],dp[x][y]+c)

    ans=INF
    for x,y in product(range(1,M+1),repeat=2):
        if(x*mb==y*ma): ans=min(ans,dp[x][y])
    if(ans==INF): ans=-1
    print(ans)
resolve()

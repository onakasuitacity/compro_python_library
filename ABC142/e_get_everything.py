# https://atcoder.jp/contests/abc142/tasks/abc142_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    keys=[0]*m
    cost=[0]*m
    for i in range(m):
        a,b=map(int,input().split())
        cost[i]=a
        key=0
        for c in map(int,input().split()):
            key+=(1<<c-1)
        keys[i]=key
    N=2**n
    dp=[INF]*N
    dp[0]=0
    for k in range(N):
        for i in range(m):
            dp[k|keys[i]]=min(dp[k|keys[i]],dp[k]+cost[i])
    print(dp[N-1] if dp[N-1]!=INF else -1)
resolve()

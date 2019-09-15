# https://atcoder.jp/contests/abc118/tasks/abc118_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    W=[0,2,5,5,4,5,6,3,7,6]
    n,m=map(int,input().split())
    A=list(map(int,input().split()))
    dp=[-1]*(n+1)
    dp[0]=0
    from itertools import product
    for i,a in product(range(n+1),A):
        if i-W[a]<0: continue
        dp[i]=max(dp[i],dp[i-W[a]]*10+a)
    print(dp[n])

resolve()

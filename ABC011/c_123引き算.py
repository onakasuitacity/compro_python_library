# https://atcoder.jp/contests/abc011/tasks/abc011_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n=int(input())
    A=[int(input()) for _ in range(3)]
    dp=[INF]*(n+5)
    dp[n]=0
    if n in A:
        print("NO")
        return
    for i in reversed(range(n+1)):
        if i in A: continue
        dp[i]=min(dp[i],dp[i+1]+1,dp[i+2]+1,dp[i+3]+1)
    print("YES" if dp[0]<=100 else "NO")

resolve()

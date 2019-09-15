# https://atcoder.jp/contests/dp/tasks/dp_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
# input=sys.stdin.readline
def resolve():
    n=int(input())
    H=list(map(int,input().split()))
    dp=[0]*n
    dp[1]=abs(H[1]-H[0])
    for i in range(2,n):
        dp[i]=min(dp[i-1]+abs(H[i]-H[i-1]),dp[i-2]+abs(H[i]-H[i-2]))
    print(dp[n-1])
resolve()

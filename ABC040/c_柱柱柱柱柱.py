# https://atcoder.jp/contests/abc040/tasks/abc040_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
# input=sys.stdin.readline
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    dp=[0]*n
    dp[1]=abs(A[1]-A[0])
    for i in range(2,n):
        dp[i]=min(dp[i-1]+abs(A[i]-A[i-1]),dp[i-2]+abs(A[i]-A[i-2]))
    print(dp[n-1])
resolve()

# https://atcoder.jp/contests/abc141/tasks/abc141_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
# input=sys.stdin.readline
def resolve():
    n=int(input())
    s=input()
    dp=[[0]*(n+1) for _ in range(n+1)]
    from itertools import product
    for i,j in product(reversed(range(n)),repeat=2):
        if i>=j: continue # i<j
        if s[i]==s[j]:
            dp[i][j]=dp[i+1][j+1]+1
        else:
            dp[i][j]=0
    ans=0
    for i,j in product(reversed(range(n)),repeat=2):
        if i>=j: continue
        ans=max(ans,min(j-i,dp[i][j]))
    print(ans)
resolve()

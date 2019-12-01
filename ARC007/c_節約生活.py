# https://atcoder.jp/contests/arc007/tasks/arc007_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    S=list(input())
    n=len(S)
    N=2**n
    for i in range(n):
        S[i]='1' if(S[i]=='o') else '0'
    S=int(''.join(S),2)
    mask=N-1

    dp=[INF]*N
    dp[0]=0
    for v in range(N):
        for i in range(n):
            u=((S<<i)+(S>>(n-i)))&mask
            dp[v|u]=min(dp[v|u],dp[v]+1)
    print(dp[-1])
resolve()

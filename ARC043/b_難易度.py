# https://atcoder.jp/contests/arc043/tasks/arc043_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    D=[int(input()) for _ in range(n)]

    V=100000
    dp=[0]*(V+1)
    for d in D:
        dp[d]+=1

    for j in range(3):
        for i in range(V):
            dp[i+1]+=dp[i]
        ndp=[0]*(V+1)
        for d in D:
            ndp[d]+=dp[d//2]
        dp=ndp

    print(sum(dp)%MOD)
resolve()

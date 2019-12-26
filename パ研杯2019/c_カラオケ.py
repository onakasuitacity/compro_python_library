# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    A=[list(map(int,input().split())) for _ in range(n)]

    ans=-INF
    for t in range(m):
        for s in range(t):
            score=0
            for i in range(n):
                score+=max(A[i][s],A[i][t])
            ans=max(ans,score)

    print(ans)
resolve()

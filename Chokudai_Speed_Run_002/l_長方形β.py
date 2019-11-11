# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_l
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from bisect import bisect_left as bisect
    n=int(input())
    AB=[0]*n
    for i in range(n):
        a,b=map(int,input().split())
        if(a>b): a,b=b,a # a <= b
        AB[i]=(a,b)
    AB.sort(lambda x:(x[0],-x[1]))

    dp=[INF]*(n+1)
    for a,b in AB:
        i=bisect(dp,b)
        dp[i]=b
    print(dp.index(INF))
resolve()

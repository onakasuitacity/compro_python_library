# https://atcoder.jp/contests/abc060/tasks/arc073_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

from collections import defaultdict
def resolve():
    n,W=map(int,input().split())
    WV=[tuple(map(int,input().split())) for _ in range(n)]

    weight=set()
    for i in range(n+1):
        if(WV[0][0]*i>W): break
        for j in range(3*i+1):
            if(WV[0][0]*i+j>W): break
            weight.add(WV[0][0]*i+j)
    weight=sorted(weight)

    dp=defaultdict(int)
    for i in range(n):
        ndp=defaultdict(int)
        w,v=WV[i]
        for key in weight:
            ndp[key]=max(ndp[key],dp[key])
            if(key+w<=W): ndp[key+w]=max(ndp[key+w],dp[key]+v)
        dp=ndp

    print(max(dp.values()))
resolve()

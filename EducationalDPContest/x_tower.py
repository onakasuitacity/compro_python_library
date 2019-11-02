# https://atcoder.jp/contests/dp/tasks/dp_x
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from functools import cmp_to_key
    n=int(input())
    B=[list(map(int,input().split())) for _ in range(n)]
    def cmp(a,b):
        va=min(a[1],b[1]-a[0])
        vb=min(b[1],a[1]-b[0])
        if(va==vb): return 0
        return -1 if(va>vb) else 1
    B.sort(key=cmp_to_key(cmp))
    maxS=20000
    dp=[-INF]*(maxS+1)
    dp[0]=0
    for i in range(n):
        w,s,v=B[i]
        ndp=dp[:]
        for total in range(maxS+1):
            if(total<=s and total+s<=maxS):
                ndp[total+w]=max(ndp[total+w],dp[total]+v)
        dp=ndp[:]
    print(max(dp))
resolve()

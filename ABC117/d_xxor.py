# https://atcoder.jp/contests/abc117/tasks/abc117_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from itertools import product
    n,k=map(int,input().split())
    cnt=[0]*40
    for a in map(int,input().split()):
        for d in range(40):
            cnt[d]+=(a>>d)&1
    dp=[0,-INF]
    for d in range(39,-1,-1):
        kb=(k>>d)&1
        newdp=[0,-INF]
        for lt,x in product(range(2),repeat=2):
            nlt=lt
            if(lt==0 and x>kb): continue
            if(x<kb): nlt=1
            newdp[nlt]=max(newdp[nlt],dp[lt]+(n-cnt[d] if(x) else cnt[d])*(1<<d))
        dp=newdp
    print(max(dp))
resolve()

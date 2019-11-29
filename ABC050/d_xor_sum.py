# https://atcoder.jp/contests/abc050/tasks/arc066_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from itertools import product
def resolve():
    n=int(input())
    dp=[1,0,0]
    for d in range(60,-1,-1):
        ndp=[0]*3
        nd=(n>>d)&1
        for s,ad,bd in product(range(3),range(2),range(2)):
            if(ad>bd): continue
            ns=min(2,2*s+nd-(ad+bd))
            if(ns<0): continue
            ndp[ns]+=dp[s]
            ndp[ns]%=MOD
        dp=ndp
    print(sum(dp)%MOD)    
resolve()

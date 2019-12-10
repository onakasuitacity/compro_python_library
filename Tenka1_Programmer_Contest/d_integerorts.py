# https://atcoder.jp/contests/tenka1-2017/tasks/tenka1_2017_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    k+=1
    AB=[tuple(map(int,input().split())) for _ in range(n)]

    dp=[0]*35 # dp[d]: less than が確定するのが d 桁目のときの最大値
    # dp[d] の状態のものが a を買えるのは、d 以上の桁については ad<=kd かつ、
    # d 桁目については ad<kd となるもののみ
    for a,b in AB:
        for d in range(34,-1,-1):
            kd=(k>>d)&1
            ad=(a>>d)&1
            if(ad>kd): break
            if(ad<kd):
                dp[d]=dp[d]+b

    print(max(dp))
resolve()

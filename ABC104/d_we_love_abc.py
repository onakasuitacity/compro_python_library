# https://atcoder.jp/contests/abc104/tasks/abc104_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    S=input()
    n=len(S)
    dp=[0]*4
    dp[0]=1
    for s in S:
        ndp=dp[:] if(s!='?') else [3*d%MOD for d in dp]
        if(s=='A' or s=='?'):
            ndp[1]+=dp[0]
            ndp[1]%=MOD
        if(s=='B' or s=='?'):
            ndp[2]+=dp[1]
            ndp[2]%=MOD
        if(s=='C' or s=='?'):
            ndp[3]+=dp[2]
            ndp[3]%=MOD
        dp=ndp
    print(dp[3])
resolve()

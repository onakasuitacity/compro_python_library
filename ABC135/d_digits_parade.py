# https://atcoder.jp/contests/abc135/tasks/abc135_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    M=13
    S=input()[::-1]
    n=len(S)
    dp=[0]*M
    dp[0]=1
    for i in range(n):
        ndp=[0]*M
        s=S[i]
        d=pow(10,i,M) # d=10^i mod 13
        if(s=='?'):
            for j in range(10):
                for m in range(M):
                    ndp[(m+j*d)%M]+=dp[m]
                    ndp[(m+j*d)%M]%=MOD
        else:
            s=int(s)
            for m in range(M):
                ndp[(m+s*d)%M]+=dp[m]
        dp=ndp
    print(dp[5])
resolve()

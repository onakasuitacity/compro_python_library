# https://atcoder.jp/contests/dp/tasks/dp_t
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    s=input()
    dp=[1]*n
    for i in range(1,n):
        ndp=[0]*n
        S=[0]*(n+1)
        for j in range(n):
            S[j+1]=S[j]+dp[j]
        for less in range(n-i):
            if(s[i-1]=='<'): ndp[less]=S[less+1]
            else: ndp[less]=S[n]-S[less+1]
            ndp[less]%=MOD
        dp=ndp
    print(dp[0])
resolve()

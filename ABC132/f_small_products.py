# https://atcoder.jp/contests/abc132/tasks/abc132_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    s=set()
    for i in range(1,1+int(n**.5)):
        s.add(i)
        s.add(n//i)
    A=sorted(s)
    m=len(A)
    coef=[0]*m
    coef[0]=1
    for i in range(1,m):
        coef[i]=A[i]-A[i-1]
    dp=[0]*m
    dp[0]=1
    for i in range(k):
        for j in range(m-1):
            dp[j+1]+=dp[j]
            dp[j+1]%=MOD
        ndp=[0]*m
        for j in range(m):
            ndp[j]=dp[m-j-1]*coef[j]
            ndp[j]%=MOD
        dp=ndp
    print(sum(dp)%MOD)
resolve()

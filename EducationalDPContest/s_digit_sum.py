# https://atcoder.jp/contests/dp/tasks/dp_s
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    k=input()
    d=int(input())
    n=len(k)
    dp=[[[0]*2 for _ in range(d)] for _ in range(n+1)]
    dp[0][0][0]=1
    for i in range(n):
        a=int(k[i])
        for j in range(d):
            for o in range(10):
                dp[i+1][(j+o)%d][1]+=dp[i][j][1]
                dp[i+1][(j+o)%d][1]%=MOD
                if(o<a):
                    dp[i+1][(j+o)%d][1]+=dp[i][j][0]
                    dp[i+1][(j+o)%d][1]%=MOD
                elif(o==a):
                    dp[i+1][(j+o)%d][0]+=dp[i][j][0]
                    dp[i+1][(j+o)%d][0]%=MOD
    print((dp[n][0][0]+dp[n][0][1]-1)%MOD)
resolve()

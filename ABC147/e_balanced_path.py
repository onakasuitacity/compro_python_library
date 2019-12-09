# https://atcoder.jp/contests/abc147/tasks/abc147_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    h,w=map(int,input().split())
    A=[list(map(int,input().split())) for _ in range(h)]
    B=[list(map(int,input().split())) for _ in range(h)]
    dp=[[0]*w for _ in range(h)]
    x=abs(A[0][0]-B[0][0])
    offset=12800
    dp[0][0]|=1<<(x+offset)
    dp[0][0]|=1<<(-x+offset)

    from itertools import product
    for i,j in product(range(h),range(w)):
        if(i==0 and j==0): continue
        x=abs(A[i][j]-B[i][j])
        S=0
        if(i>0): S|=dp[i-1][j]
        if(j>0): S|=dp[i][j-1]
        dp[i][j]=(S<<x)|(S>>x)

    for i in range(12800):
        if((dp[-1][-1]>>(i+offset))&1):
            print(i)
            return
resolve()

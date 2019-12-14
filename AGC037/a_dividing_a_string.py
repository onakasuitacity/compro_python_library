# https://atcoder.jp/contests/agc037/tasks/agc037_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    S=input()
    n=len(S)
    if(n==1):
        print(1)
        return

    # dp
    S='#'+S # 1-indexed
    dp1=[0]*(n+1)
    dp2=[0]*(n+1)
    dp1[1]=1
    dp2[2]=1
    if(S[0]==S[1]): dp1[2]=2

    for i in range(2,n+1):
        if(S[i]!=S[i-1]):
            dp1[i]=max(dp1[i-1],dp2[i-1])+1
        else:
            dp1[i]=dp2[i-1]+1
        dp2[i]=dp1[i-2]+1

    print(max(dp1[-1],dp2[-1]))
resolve()

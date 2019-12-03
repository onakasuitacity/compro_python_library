# https://atcoder.jp/contests/abc023/tasks/abc023_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    maxR,maxC,k=map(int,input().split())
    n=int(input())
    RC=[None]*n
    R=[0]*maxR
    C=[0]*maxC
    for i in range(n):
        r,c=map(int,input().split())
        r-=1; c-=1
        RC[i]=(r,c)
        R[r]+=1
        C[c]+=1

    DC=[0]*(n+1)
    for c in C:
        DC[c]+=1

    ans=0
    for r in R:
        if(r>k): continue
        ans+=DC[k-r]

    for r,c in RC:
        if(R[r]+C[c]==k): ans-=1
        if(R[r]+C[c]==k+1): ans+=1
    print(ans)
resolve()

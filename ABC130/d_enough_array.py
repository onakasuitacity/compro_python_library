# https://atcoder.jp/contests/abc130/tasks/abc130_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    ans=0
    r=0
    sum=0
    for l in range(n):
        while(r<n and sum+A[r]<k):
            sum+=A[r]
            r+=1
        ans+=r-l
        if(r==l):
            r+=1
        else:
            sum-=A[l]
    print(n*(n+1)//2-ans)
resolve()

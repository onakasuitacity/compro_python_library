# https://atcoder.jp/contests/abc030/tasks/abc030_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from bisect import bisect_left
    n,m=map(int,input().split())
    x,y=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    now=0
    ans=0
    count=0
    while(True):
        i=bisect_left(A,now)
        if i==n: break
        now=A[i]+x
        j=bisect_left(B,now)
        if j==m: break
        now=B[j]+y
        ans+=1
    print(ans)
resolve()

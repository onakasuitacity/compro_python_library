# https://atcoder.jp/contests/abc014/tasks/abc014_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,x=map(int,input().split())
    A=list(map(int,input().split()))
    ans=0
    for d in range(n-1,-1,-1):
        if((x>>d)&1): ans+=A[d]
    print(ans)
resolve()

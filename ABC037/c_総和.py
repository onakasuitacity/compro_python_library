# https://atcoder.jp/contests/abc037/tasks/abc037_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    for i in range(n-1):
        A[i+1]+=A[i]
    ans=A[k-1]
    for i in range(1,n-k+1):
        ans+=A[k+i-1]-A[i-1]
    print(ans)
resolve()

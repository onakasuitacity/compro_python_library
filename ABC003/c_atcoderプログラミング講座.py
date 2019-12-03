# https://atcoder.jp/contests/abc003/tasks/abc003_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    R=list(map(int,input().split()))
    R.sort()
    ans=0
    for r in R[n-k:]:
        ans=(ans+r)/2
    print(ans)
resolve()

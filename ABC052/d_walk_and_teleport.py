# https://atcoder.jp/contests/abc052/tasks/arc067_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,a,b=map(int,input().split())
    X=list(map(int,input().split()))
    ans=0
    for i in range(n-1):
        ans+=min(b,a*(X[i+1]-X[i]))
    print(ans)
resolve()

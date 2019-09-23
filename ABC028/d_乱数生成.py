# https://atcoder.jp/contests/abc028/tasks/abc028_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    ans=0
    # 1<=i<k<j<=n
    ans+=6*(1/n)*((k-1)/n)*((n-k)/n)
    # 1<=k=k<j<=n or 1<=j<k=k<=n
    ans+=3*(1/n)*(1/n)*((n-1)/n)
    # 1<=k=k=k<=n
    ans+=(1/n)*(1/n)*(1/n)
    print(ans)
resolve()

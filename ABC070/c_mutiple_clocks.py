# https://atcoder.jp/contests/abc070/tasks/abc070_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
# input=sys.stdin.readline
def resolve():
    n=int(input())
    ans=1
    from fractions import gcd
    for _ in range(n):
        t=int(input())
        ans=ans*t//(gcd(ans,t))
    print(ans)
resolve()

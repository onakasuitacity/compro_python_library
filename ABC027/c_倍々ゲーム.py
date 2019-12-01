# https://atcoder.jp/contests/abc027/tasks/abc027_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    n-=1
    r=4
    while(n>=2*r):
        n-=2*r
        r*=4
    print("Takahashi" if(1<=n<=r) else "Aoki")
resolve()

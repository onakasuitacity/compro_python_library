# https://atcoder.jp/contests/agc018/tasks/agc018_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from fractions import gcd
def resolve():
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    m=max(A)
    g=0
    for a in A:
        g=gcd(g,a)

    print("POSSIBLE" if(k%g==0 and k<=m) else "IMPOSSIBLE")
resolve()

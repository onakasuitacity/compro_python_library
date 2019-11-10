# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_g
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from fractions import gcd
    n=int(input())
    for _ in range(n):
        a,b=map(int,input().split())
        print(gcd(a,b))
resolve()

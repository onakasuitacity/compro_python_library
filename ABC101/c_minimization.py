# https://atcoder.jp/contests/abc101/tasks/arc099_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from math import ceil
    n,k=map(int,input().split())
    print(ceil((n-1)/(k-1)))
resolve()

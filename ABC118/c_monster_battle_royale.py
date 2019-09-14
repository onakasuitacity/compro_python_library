# https://atcoder.jp/contests/abc118/tasks/abc118_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n=int(input())
    A=map(int,input().split())
    from fractions import gcd
    from functools import reduce
    print(reduce(gcd,A))
resolve()

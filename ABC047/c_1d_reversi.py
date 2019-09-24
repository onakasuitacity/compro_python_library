# https://atcoder.jp/contests/abc047/tasks/arc063_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from itertools import groupby
    print(len(list(groupby(input())))-1)
resolve()

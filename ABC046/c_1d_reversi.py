# https://atcoder.jp/contests/abc047/tasks/arc063_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from itertools import groupby
def resolve():
    S=input()
    print(len(tuple(groupby(S)))-1)
resolve()

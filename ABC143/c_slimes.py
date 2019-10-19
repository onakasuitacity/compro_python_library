# https://atcoder.jp/contests/abc143/tasks/abc143_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    input()
    s=input()
    from itertools import groupby
    print(len(list(groupby(s))))
resolve()

# https://atcoder.jp/contests/abc131/tasks/abc131_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from itertools import groupby
    G=groupby(input())
    print("Good" if(len(list(G))==4) else "Bad")
resolve()

# https://atcoder.jp/contests/abc029/tasks/abc029_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    from itertools import product
    for S in product("abc",repeat=n):
        print(''.join(S))
resolve()

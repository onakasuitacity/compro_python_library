# https://atcoder.jp/contests/abc134/tasks/abc134_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from math import ceil
    n,d=map(int,input().split())
    print(ceil(n/(2*d+1)))
resolve()

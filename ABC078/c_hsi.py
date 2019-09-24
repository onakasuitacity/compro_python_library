# https://atcoder.jp/contests/abc078/tasks/arc085_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    print((2**m)*(100*n+1800*m))
resolve()

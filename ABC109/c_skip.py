# https://atcoder.jp/contests/abc109/tasks/abc109_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n,x=map(int,input().split())
    A=list(map(lambda y:int(y)-x,input().split()))
    if n==1:
        print(abs(A[0]))
        return
    from fractions import gcd
    from functools import reduce
    print(abs(reduce(gcd,A)))
resolve()

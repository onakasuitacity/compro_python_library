# https://atcoder.jp/contests/arc006/tasks/arc006_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from bisect import bisect_left
def resolve():
    n=int(input())
    A=[INF]*(n+1)
    for _ in range(n):
        w=int(input())
        i=bisect_left(A,w)
        A[i]=w

    print(A.index(INF))
resolve()

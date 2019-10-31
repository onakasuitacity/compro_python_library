# https://atcoder.jp/contests/abc006/tasks/abc006_4
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from bisect import bisect_left as bisect
    n=int(input())
    A=[int(input()) for _ in range(n)]
    B=[INF]*n
    for a in A:
        i=bisect(B,a)
        B[i]=a
    print(n-bisect(B,n+1))
resolve()

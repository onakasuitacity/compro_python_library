# https://atcoder.jp/contests/chokudai_s001/tasks/chokudai_S001_h
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from bisect import bisect_left
    n=int(input())
    A=list(map(int,input().split()))
    B=[INF]*(n+1)
    for a in A:
        i=bisect_left(B,a)
        B[i]=a
    i=B.index(INF)
    print(i)
resolve()

# https://atcoder.jp/contests/abc038/tasks/abc038_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from bisect import bisect_left as bisect
def resolve():
    n=int(input())
    X=[INF]*(n+1)
    WH=[tuple(map(int,input().split())) for _ in range(n)]
    WH.sort(lambda x:(x[0],-x[1]))
    for w,h in WH:
        i=bisect(X,h)
        X[i]=h
    print(X.index(INF))
resolve()

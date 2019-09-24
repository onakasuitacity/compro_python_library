# https://atcoder.jp/contests/abc012/tasks/abc012_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    h=str(n//3600).zfill(2)
    n%=3600
    m=str(n//60).zfill(2)
    s=str(n%60).zfill(2)
    print(h,m,s,sep=":")
resolve()

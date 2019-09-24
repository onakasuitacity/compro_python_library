# https://atcoder.jp/contests/abc030/tasks/abc030_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    n%=12
    a=6*m
    b=30*n+m/2
    c=abs(a-b)
    print(min(c,360-c))
resolve()

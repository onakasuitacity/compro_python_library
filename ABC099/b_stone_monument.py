# https://atcoder.jp/contests/abc099/tasks/abc099_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b=map(int,input().split())
    n=b-a
    print(n*(n-1)//2-a)
resolve()

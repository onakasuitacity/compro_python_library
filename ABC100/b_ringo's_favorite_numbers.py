# https://atcoder.jp/contests/abc100/tasks/abc100_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    d,n=map(int,input().split())
    print(n*(100**d) if n!=100 else 101*(100**d))
resolve()

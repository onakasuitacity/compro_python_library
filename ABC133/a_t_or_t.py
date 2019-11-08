# https://atcoder.jp/contests/abc133/tasks/abc133_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,a,b=map(int,input().split())
    print(min(n*a,b))
resolve()

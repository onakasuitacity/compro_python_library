# https://atcoder.jp/contests/abc090/tasks/arc091_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    print(abs(n-2)*abs(m-2))
resolve()

# https://atcoder.jp/contests/abc143/tasks/abc143_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
# input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b=map(int,input().split())
    print(max(0,a-2*b))
resolve()

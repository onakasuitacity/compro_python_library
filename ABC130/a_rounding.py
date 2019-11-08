# https://atcoder.jp/contests/abc130/tasks/abc130_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    x,a=map(int,input().split())
    if(x<a):
        print(0)
    else:
        print(10)
resolve()

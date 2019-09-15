# https://atcoder.jp/contests/abc137/tasks/abc137_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    k,x=map(int,input().split())
    print(*range(x-k+1,x+k))
resolve()

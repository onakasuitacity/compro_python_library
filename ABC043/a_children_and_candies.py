# https://atcoder.jp/contests/abc043/tasks/abc043_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    print(n*(n+1)//2)
resolve()

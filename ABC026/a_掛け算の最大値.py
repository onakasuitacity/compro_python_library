# https://atcoder.jp/contests/abc026/tasks/abc026_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a=int(input())
    print((a//2)**2)
resolve()

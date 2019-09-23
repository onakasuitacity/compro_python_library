# https://atcoder.jp/contests/abc045/tasks/abc045_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b,h=[int(input()) for _ in range(3)]
    print((a+b)*h//2)
resolve()

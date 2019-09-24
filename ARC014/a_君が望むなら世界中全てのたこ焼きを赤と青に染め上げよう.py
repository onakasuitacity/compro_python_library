# https://atcoder.jp/contests/arc014/tasks/arc014_1
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    print("Red" if n%2 else "Blue")
resolve()

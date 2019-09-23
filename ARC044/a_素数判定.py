# https://atcoder.jp/contests/arc044/tasks/arc044_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    if n==1:
        print("Not Prime")
    elif n in (2,3,5):
        print("Prime")
    else:
        print("Prime" if all((n%2,n%3,n%5)) else "Not Prime")
resolve()

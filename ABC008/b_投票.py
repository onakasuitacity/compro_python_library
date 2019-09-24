# https://atcoder.jp/contests/abc008/tasks/abc008_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    from collections import Counter
    C=Counter([input() for _ in range(n)]).most_common()
    print(C[0][0])
resolve()
